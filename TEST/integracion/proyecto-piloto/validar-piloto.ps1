$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$projectRoot = Join-Path $repoRoot 'LIBROS\activos\PID-PILOTO-001'
$statePath = Join-Path $projectRoot '_meta\estado.json'
$state = Get-Content -Raw -LiteralPath $statePath | ConvertFrom-Json
$results = [System.Collections.Generic.List[object]]::new()

function Add-Result {
    param([string]$Id, [bool]$Passed, [string]$Evidence)
    $results.Add([pscustomobject]@{ Id = $Id; Passed = $Passed; Evidence = $Evidence })
}

function Test-ArtifactSet {
    param([string]$StateName, [string[]]$Available)
    $required = @($state.required_artifacts.$StateName)
    return @($required | Where-Object { $_ -notin $Available }).Count -eq 0
}

function Invoke-SimulatedTransition {
    param(
        [string]$From,
        [string]$To,
        [string[]]$Available,
        [string]$Gate = 'NO_APLICA',
        [string]$HumanApproval = 'NO_APLICA'
    )

    if (-not (Test-ArtifactSet -StateName $From -Available $Available)) {
        return 'BLOQUEADO_ARTEFACTOS'
    }
    if ($Gate -match '^GR-[1-4]$' -and $HumanApproval -ne 'APROBADO') {
        return 'BLOQUEADO_PUERTA_HUMANA'
    }
    return "AVANZA_A_$To"
}

$expectedDirectories = @(
    '_meta', 'brief', 'investigacion', 'arquitectura', 'assets_creativos',
    'manuscrito', 'edicion', 'produccion', 'publicacion',
    'postpublicacion', 'checkpoints'
)
$missingDirectories = @($expectedDirectories | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $projectRoot $_) -PathType Container)
})
Add-Result 'PIL-001' ($missingDirectories.Count -eq 0) "directorios ausentes: $($missingDirectories -join ', ')"

Add-Result 'PIL-002' (
    $state.project_id -eq 'PID-PILOTO-001' -and
    $state.initial_state -eq 'IDEA' -and
    $state.current_state -eq 'IDEA' -and
    $state.simulation -and
    -not $state.publishable
) 'estado persistido IDEA y simulación no publicable'

$allRequired = @()
foreach ($property in $state.required_artifacts.PSObject.Properties) {
    $allRequired += @($property.Value)
}
$missingArtifacts = @($allRequired | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $projectRoot $_) -PathType Leaf)
})
Add-Result 'PIL-003' ($missingArtifacts.Count -eq 0) "artefactos ausentes: $($missingArtifacts -join ', ')"

$ideaComplete = @($state.required_artifacts.IDEA)
$ideaIncomplete = @('brief/brief_v01.md')
$advanceComplete = Invoke-SimulatedTransition -From 'IDEA' -To 'INVESTIGACION' -Available $ideaComplete
$advanceIncomplete = Invoke-SimulatedTransition -From 'IDEA' -To 'INVESTIGACION' -Available $ideaIncomplete
Add-Result 'PIL-004' (
    $advanceComplete -eq 'AVANZA_A_INVESTIGACION' -and
    $advanceIncomplete -eq 'BLOQUEADO_ARTEFACTOS'
) 'avance condicionado a artefactos obligatorios'

$assetsComplete = @($state.required_artifacts.CREACION_ASSETS)
$gateBlocked = Invoke-SimulatedTransition -From 'CREACION_ASSETS' -To 'REDACCION' -Available $assetsComplete -Gate 'GR-2' -HumanApproval 'PENDIENTE'
$gateApproved = Invoke-SimulatedTransition -From 'CREACION_ASSETS' -To 'REDACCION' -Available $assetsComplete -Gate 'GR-2' -HumanApproval 'APROBADO'
Add-Result 'PIL-005' (
    $gateBlocked -eq 'BLOQUEADO_PUERTA_HUMANA' -and
    $gateApproved -eq 'AVANZA_A_REDACCION'
) 'GR-2 no puede omitirse'

$rejectionTarget = $state.human_gates.'GR-2'.rejection_target
Add-Result 'PIL-006' ($rejectionTarget -eq 'ARQUITECTURA') 'rechazo GR-2 devuelve a ARQUITECTURA'

$attempts = 1..3
$retryResult = if ($attempts.Count -ge $state.max_retries) { 'ESCALADO' } else { 'REINTENTO' }
Add-Result 'PIL-007' ($retryResult -eq 'ESCALADO') 'tres reintentos producen escalado'

$log = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'log.md')
$loggedEvents = @('creación del expediente', 'creación de checkpoint inicial', 'preparación de artefactos', 'ejecución de pruebas')
$missingEvents = @($loggedEvents | Where-Object { $log -notmatch [regex]::Escape($_) })
Add-Result 'PIL-008' ($missingEvents.Count -eq 0) 'acciones documentales registradas'

$v01 = Join-Path $projectRoot 'manuscrito\ms_capitulo_01_v01.md'
$v02 = Join-Path $projectRoot 'manuscrito\ms_capitulo_01_v02.md'
$differentVersions = (Test-Path -LiteralPath $v01) -and (Test-Path -LiteralPath $v02) -and
    ((Get-FileHash -LiteralPath $v01).Hash -ne (Get-FileHash -LiteralPath $v02).Hash)
Add-Result 'PIL-009' $differentVersions 'v01 y v02 coexisten y difieren'

$cp0 = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'checkpoints\CP-000-IDEA.json') | ConvertFrom-Json
$cp1 = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'checkpoints\CP-001-ARQUITECTURA-SIMULADA.json') | ConvertFrom-Json
Add-Result 'PIL-010' (
    $cp0.state -eq 'IDEA' -and
    $cp1.restore_target -eq 'CP-000' -and
    $cp1.previous_checkpoint -eq 'CP-000'
) 'checkpoint simulado declara retorno a IDEA'

$persistedAfterTests = Get-Content -Raw -LiteralPath $statePath | ConvertFrom-Json
Add-Result 'PIL-011' ($persistedAfterTests.current_state -eq 'IDEA') 'las pruebas no mutan el expediente'

$failed = @($results | Where-Object { -not $_.Passed })
$results | ForEach-Object {
    $status = if ($_.Passed) { 'SUPERADA' } else { 'FALLIDA' }
    Write-Output "$($_.Id) $status - $($_.Evidence)"
}

if ($failed.Count -gt 0) {
    exit 1
}

Write-Output "RESULTADO: SUPERADA ($($results.Count)/$($results.Count))"

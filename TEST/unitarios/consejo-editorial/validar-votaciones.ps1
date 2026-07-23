$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$schemaPath = Join-Path $repoRoot 'PLANTILLAS\votacion-consejo.schema.json'
$fixturesPath = Join-Path $repoRoot 'TEST\casos_prueba\consejo-editorial'
$expectedMembers = @('GOB-02a', 'GOB-02b', 'GOB-02c', 'GOB-02d')
$expected = @{
    '4-0' = @{ Result = 'APROBAR'; Dissent = $false; Human = $true }
    '3-1' = @{ Result = 'APROBAR'; Dissent = $true; Human = $true }
    '2-2' = @{ Result = 'REQUIERE_CAMBIOS'; Dissent = $true; Human = $true }
    '1-3' = @{ Result = 'RECHAZAR'; Dissent = $true; Human = $true }
    '0-4' = @{ Result = 'RECHAZAR'; Dissent = $false; Human = $false }
}

Get-Content -Raw -LiteralPath $schemaPath | ConvertFrom-Json | Out-Null
$failures = [System.Collections.Generic.List[string]]::new()
$files = Get-ChildItem -LiteralPath $fixturesPath -Filter '*.json' | Sort-Object Name

if ($files.Count -ne 5) {
    $failures.Add("Se esperaban 5 ejemplos y se encontraron $($files.Count).")
}

foreach ($file in $files) {
    $record = Get-Content -Raw -LiteralPath $file.FullName | ConvertFrom-Json
    $members = @($record.votes.PSObject.Properties.Name)

    if (@(Compare-Object $expectedMembers $members).Count -ne 0) {
        $failures.Add("$($file.Name): miembros ausentes, duplicados o inesperados.")
    }

    $approveCount = 0
    foreach ($member in $expectedMembers) {
        $vote = $record.votes.$member
        if ($vote.vote -eq 'APROBAR') { $approveCount++ }
        if ([string]::IsNullOrWhiteSpace($vote.justification)) {
            $failures.Add("$($file.Name): $member no incluye justificación.")
        }
        if (@($vote.norm_refs).Count -lt 1) {
            $failures.Add("$($file.Name): $member no incluye referencias normativas.")
        }
        if (-not $vote.sealed -or $vote.saw_other_votes) {
            $failures.Add("$($file.Name): $member incumple la independencia.")
        }
    }

    $rule = "$approveCount-$($expectedMembers.Count - $approveCount)"
    $expectation = $expected[$rule]
    if ($record.consolidation.rule -ne $rule -or
        $record.consolidation.approve_count -ne $approveCount -or
        $record.consolidation.non_approve_count -ne (4 - $approveCount) -or
        $record.consolidation.result -ne $expectation.Result -or
        $record.consolidation.dissent -ne $expectation.Dissent -or
        $record.consolidation.requires_human_review -ne $expectation.Human) {
        $failures.Add("$($file.Name): consolidación incorrecta para $rule.")
    }

    if ($record.gate -match '^GR-[1-4]$' -and
        (-not $record.human_approval.required -or $record.human_approval.status -ne 'PENDIENTE')) {
        $failures.Add("$($file.Name): la puerta humana no permanece pendiente.")
    }
}

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Output "SUPERADA: $($files.Count) ejemplos; votos independientes, justificados, referenciados y consolidados correctamente."

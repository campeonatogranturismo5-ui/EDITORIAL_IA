# Eventos de agentes

`agent-events.jsonl` contiene una entrada JSON UTF-8 por ejecución final del runner.
El escritor añade registros sin sobrescribir los anteriores, enmascara secretos y
calcula un checksum SHA-256 verificable.

Este almacenamiento es local y de desarrollo; no sustituye un sistema transaccional
o firmado de auditoría de producción.

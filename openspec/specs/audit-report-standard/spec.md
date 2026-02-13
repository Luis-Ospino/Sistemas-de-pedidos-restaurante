# audit-report-standard Specification

## Purpose
Define the required structure and traceability rules for `AUDITORIA.md` so findings can be tracked across audit phases and implementation evidence.

## Requirements

### Requirement: AUDITORIA.md uses a standard finding structure
El archivo `AUDITORIA.md` SHALL registrar cada hallazgo con: componente afectado, evidencia tecnica, principio vulnerado o code smell, impacto y recomendacion.

#### Scenario: New finding is documented
- **WHEN** un integrante agrega un hallazgo a `AUDITORIA.md`
- **THEN** el registro contiene todos los campos requeridos por la plantilla

### Requirement: Audit report links findings to next phases
`AUDITORIA.md` SHALL incluir trazabilidad de hallazgos priorizados hacia decisiones de patrones (Fase 2), tareas de refactorizacion (Fase 3) y deuda tecnica gestionada (Fase 5).

#### Scenario: Team plans phase-2 work
- **WHEN** el equipo selecciona patrones de diseno
- **THEN** puede mapear cada decision a hallazgos concretos del reporte de auditoria

#### Scenario: Team plans technical debt payment
- **WHEN** un hallazgo permanece abierto o parcialmente mitigado
- **THEN** `AUDITORIA.md` referencia el identificador `DT-*` correspondiente en `DEUDA_TECNICA.md`

### Requirement: Audit baseline is preserved
La auditoria SHALL referenciar el snapshot base post-MVP para permitir comparacion de evolucion arquitectonica en fases posteriores.

#### Scenario: Team reviews evolution
- **WHEN** se compara el estado tras refactorizaciones
- **THEN** el equipo puede contrastar contra el snapshot base documentado

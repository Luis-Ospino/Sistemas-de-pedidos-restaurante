# AUDITORIA Fase 1 - Preparacion

Estado: PREPARADO (pendiente ejecutar hallazgos)

## Baseline

- Commit snapshot post-MVP: `51b8f5d` (`audit: snapshot post-mvp`)
- Rama de trabajo de auditoria: `feature/auditoria-fase-1-diagnostico`
- Objetivo de este documento en este cambio: dejar estructura y criterios listos para que el siguiente cambio capture hallazgos reales.

## Alcance definido

- Backend: `order-service/`, `kitchen-worker/`
- Frontend: `src/`
- Integraciones: eventos, colas y contratos entre servicios
- Flujo operativo/documental: `AI_WORKFLOW.md`, `README.md`, `docker-compose*.yml`

## Criterios de revision obligatoria

- Violaciones SOLID (minimo SRP y DIP)
- Code smells: acoplamiento rigido, logica duplicada, falta de abstraccion
- Impacto: mantenibilidad, escalabilidad, riesgo operativo
- Severidad: Alta, Media o Baja

## Plantilla de hallazgo

Usar la plantilla en `docs/auditoria/PLANTILLA_HALLAZGO.md` para cada hallazgo.

## Hallazgos

Pendiente en el siguiente cambio (`auditoria-fase-1-ejecucion`, sugerido).

## Mapeo preliminar a fases siguientes

- Fase 2 (patrones): se completara cuando existan hallazgos priorizados.
- Fase 3 (refactor): se completara cuando existan puntos de entrada definidos por hallazgo.

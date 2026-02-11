# Alcance de Auditoria - Fase 1

## Objetivo

Definir una cobertura minima comun para todo el equipo antes de ejecutar el diagnostico tecnico.

## Dominios y responsables sugeridos

- Backend (`order-service/`, `kitchen-worker/`): APIs, reglas de negocio, dependencias, eventos.
- Frontend (`src/`): componentes, hooks, servicios HTTP, estado y duplicacion de logica.
- Integracion y contratos: publicacion/consumo de eventos, DTOs, consistencia entre UI y backend.
- Operacion/documentacion: scripts, compose, workflow de IA y guias de arranque.

## Evidencia minima por hallazgo

- Ruta de archivo y componente afectado
- Fragmento o descripcion concreta del problema
- Principio vulnerado o smell identificado
- Impacto tecnico
- Recomendacion
- Severidad (Alta/Media/Baja)

## Regla de calidad de evidencia

No aceptar hallazgos sin evidencia trazable a archivo, modulo o flujo reproducible.

# Evidencia de Implementacion - H-ALTA-02

**Fecha:** 2026-02-13
**Hallazgo:** H-ALTA-02 - Gap de consistencia entre persistencia y publicacion de eventos
**Rama:** `feature/auditoria-fase-1-ejecucion`
**Estado:** COMPLETADO

---

## Defecto

El flujo de creacion de orden podia persistir datos sin garantizar publicacion de evento al fallar el broker, generando inconsistencia entre servicios.

## Resumen de solucion

Se aplico `Command Pattern` para encapsular la publicacion del evento y propagar errores de broker, permitiendo rollback transaccional del flujo de orden.

## Commits relacionados

- `82beb21` `refactor: implementado patron Command para resolver gap de consistencia en OrderService`
- `d834df8` `test: agregado coverage para comando de publicacion y manejo de falla de broker`
- `8f5e01e` `docs: documentados aciertos existentes para H-ALTA-02 en AUDITORIA`

## Archivos principales modificados

- `order-service/src/main/java/com/restaurant/orderservice/service/OrderService.java`
- `order-service/src/main/java/com/restaurant/orderservice/service/command/OrderCommand.java`
- `order-service/src/main/java/com/restaurant/orderservice/service/command/OrderCommandExecutor.java`
- `order-service/src/main/java/com/restaurant/orderservice/service/command/PublishOrderPlacedEventCommand.java`
- `order-service/src/main/java/com/restaurant/orderservice/exception/EventPublicationException.java`
- `order-service/src/main/java/com/restaurant/orderservice/exception/GlobalExceptionHandler.java`
- `order-service/src/test/java/com/restaurant/orderservice/service/OrderServiceTest.java`
- `order-service/src/test/java/com/restaurant/orderservice/service/command/PublishOrderPlacedEventCommandTest.java`

## Evidencia funcional

- La falla de publicacion ya no se ignora; se eleva excepcion de dominio para consistencia transaccional.
- `OrderService#createOrder` delega en `OrderCommandExecutor` y detiene el flujo ante error.
- `GlobalExceptionHandler` reporta `503` ante falla del broker.

## Estado

- Mitigacion implementada y versionada.
- Evidencia consolidada en `AUDITORIA.md`.
- Lista para integracion a `develop` mediante PR.

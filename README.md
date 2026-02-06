# Frontend - Sistema de Pedidos (MVP)

Este frontend implementa:
- **UI Cliente**: mesa -> menu -> carrito -> confirmacion -> consulta de estado.
- **UI Cocina**: listado de pedidos + acciones de cambio de estado (modo mock sin PIN).

Basado en el documento de requerimientos del MVP (2 dias).

## Requisitos
- Node.js 18+ (recomendado 20+)
- Docker + Docker Compose (para smoke test)

## Variables de entorno
Crea un archivo `.env` (puedes copiar desde `.env.example`) si quieres preparar futura integracion
con backend. Para modo mock no es necesario.

## Ejecutar en desarrollo (hot reload)
```bash
npm i
npm run dev
```
Abre: http://localhost:5173

## Build + preview (modo "produccion local")
```bash
npm run build
npm run preview
```
Abre: http://localhost:8080

## Smoke test con Docker Compose
1) Construir y levantar el frontend:
```bash
docker compose -f docker-compose.frontend.yml up -d --build
```

2) Probar que sirve HTML:
```bash
npm run smoke
```

3) Apagar:
```bash
docker compose -f docker-compose.frontend.yml down
```

## Integracion con API
Actualmente el frontend funciona en **modo mock**, sin llamadas a endpoints externos.
La UI usa datos en memoria y mantiene el contrato del backend:
- Estados: `PENDING`, `IN_PREPARATION`, `READY`
- ID de pedido: `id` (UUID)

Endpoints esperados para futura integracion:
- `GET /menu`
- `POST /orders`
- `GET /orders/{id}`
- `GET /orders?status=...` (cocina)
- `PATCH /orders/{id}/status` (cocina)

La base URL se configurara con `VITE_API_BASE_URL` cuando se habilite integracion real (ver `.env.example`).

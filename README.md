# 🍽️ Restaurant Order System

Full-stack restaurant ordering system with microservices architecture, React frontend, and asynchronous event-driven communication.

## 📋 Overview

**Components**
- **Frontend**: React + Vite + TypeScript + TailwindCSS
- **Order Service**: Spring Boot REST API
- **Kitchen Worker**: Spring Boot async consumer
- **RabbitMQ**: Message broker for event-driven communication
- **PostgreSQL**: Relational database
- **Docker Compose**: Full stack orchestration

**Architecture Flow**
```
Frontend → Order Service → RabbitMQ → Kitchen Worker
              ↓
         PostgreSQL
```

### Data Flow

1. **Client** → Selects table, views menu, adds items to cart
2. **Frontend** → Sends order to Order Service via REST API
3. **Order Service** → Saves order in PostgreSQL with PENDING status
4. **Order Service** → Publishes `order.placed` event to RabbitMQ
5. **Kitchen Worker** → Consumes event and updates order to IN_PREPARATION
6. **Kitchen** → Views orders in real-time and updates statuses

---

## 🚀 Quickstart (Docker Compose)

**Prerequisites**: Docker Desktop installed and running

### 1. Clone and Setup

```bash
git clone https://github.com/Luis-Ospino/Sistemas-de-pedidos-restaurante.git
cd Sistemas-de-pedidos-restaurante
```

### 2. Create Environment File

```bash
# Windows PowerShell
Copy-Item .env.example .env

# Linux/Mac
cp .env.example .env
```

The default `.env.example` works out of the box. No modifications needed.

### 3. Start the Stack

```bash
docker compose up -d --build
```

### 4. Access the Applications

Wait 30-60 seconds for all services to initialize, then access:

| Service | URL | Credentials |
|---------|-----|-------------|
| **Frontend (Client)** | http://localhost:5173 | - |
| **Frontend (Kitchen)** | http://localhost:5173/kitchen | PIN: 1234 |
| **API Backend** | http://localhost:8080 | - |
| **Swagger UI** | http://localhost:8080/swagger-ui.html | - |
| **RabbitMQ Management** | http://localhost:15672 | guest/guest |

### 5. Stop the Stack

```bash
docker compose down
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `VITE_USE_MOCK` | `false` | Use mock data (`true`) or real API (`false`) |
| `VITE_API_BASE_URL` | `http://localhost:8080` | Backend API URL |
| `VITE_KITCHEN_PIN` | `1234` | Kitchen access PIN |
| `VITE_ALLOWED_HOSTS` | - | Optional: Allowed hosts for Vite (e.g., `.trycloudflare.com`) |
| `CORS_ALLOWED_ORIGIN_PATTERNS` | - | Allowed CORS origins for API |
| `DB_URL` | `jdbc:postgresql://postgres:5432/restaurant_db` | Database JDBC URL |
| `DB_USER` / `DB_PASS` | `restaurant_user` / `restaurant_pass` | Database credentials |
| `RABBITMQ_HOST` / `RABBITMQ_PORT` | `rabbitmq` / `5672` | RabbitMQ connection |

### Ports

| Service | Port | Description |
|---------|------|-------------|
| Frontend | 5173 | React application |
| Order Service | 8080 | REST API |
| Kitchen Worker | - | Internal service (no exposed port) |
| PostgreSQL | 5432 | Database |
| RabbitMQ AMQP | 5672 | Message protocol |
| RabbitMQ Management | 15672 | Admin UI |

---

## 📱 Using the Application

### Client Interface

1. **Select Table**: Enter table number (1-20)
2. **View Menu**: Browse available products
3. **Add to Cart**: Select products and quantities
4. **Place Order**: Confirm and submit order
5. **Track Status**: View order status in real-time

### Kitchen Interface

1. **Login**: Enter PIN (default: 1234)
2. **View Orders**: List of pending and in-preparation orders
3. **Update Status**: Mark orders as ready
4. **Filter**: Filter by status (Pending, In Preparation, Ready)

---

## 🔌 API Endpoints

### Menu

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/menu` | Get list of available products |

### Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders` | Create new order |
| GET | `/orders` | List all orders |
| GET | `/orders?status=PENDING` | Filter orders by status |
| GET | `/orders/{id}` | Get order by ID |
| PATCH | `/orders/{id}/status` | Update order status |

### API Examples

**Get Menu**
```powershell
Invoke-RestMethod -Uri "http://localhost:8080/menu" -Method Get
```

**Create Order**
```powershell
$body = @{
    tableId = 5
    items = @(
        @{ productId = 1; quantity = 2; note = "Sin cebolla" },
        @{ productId = 3; quantity = 1; note = "Extra aderezo" }
    )
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8080/orders" `
  -Method Post -Body $body -ContentType "application/json"
```

**Get Order**
```powershell
Invoke-RestMethod -Uri "http://localhost:8080/orders/{orderId}" -Method Get
```

**Update Status**
```powershell
$statusUpdate = @{ status = "READY" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8080/orders/{orderId}/status" `
  -Method Patch -Body $statusUpdate -ContentType "application/json"
```

---

## 🛠️ Useful Commands

### Docker Compose

```bash
# View container status
docker compose ps

# View logs (all services)
docker compose logs -f

# View logs (specific service)
docker compose logs -f frontend
docker compose logs -f order-service
docker compose logs -f kitchen-worker

# Restart a service
docker compose restart frontend

# Stop all services
docker compose down

# Stop and remove volumes (clean slate)
docker compose down -v

# Rebuild and start
docker compose up --build
```

### RabbitMQ Verification

```bash
# View queues and messages
docker exec restaurant-rabbitmq rabbitmqctl list_queues name messages_ready messages_unacknowledged

# View active connections
docker exec restaurant-rabbitmq rabbitmqctl list_connections

# View exchanges
docker exec restaurant-rabbitmq rabbitmqctl list_exchanges
```

### Database Verification

```bash
# Connect to PostgreSQL
docker exec -it restaurant-postgres psql -U restaurant_user -d restaurant_db

# View orders
docker exec -it restaurant-postgres psql -U restaurant_user -d restaurant_db \
  -c "SELECT id, table_id, status, created_at FROM orders ORDER BY created_at DESC LIMIT 10;"

# View products
docker exec -it restaurant-postgres psql -U restaurant_user -d restaurant_db \
  -c "SELECT * FROM products;"
```

---

## 🧪 Testing

```bash
# Order Service tests
cd order-service
mvn test

# Kitchen Worker tests
cd kitchen-worker
mvn test

# Frontend tests
npm test
```

**Test Coverage**
- ✅ 29 unit tests in Order Service
- ✅ 9 unit tests in Kitchen Worker
- ✅ Controller tests
- ✅ Service tests
- ✅ Exception handling tests
- ✅ Property-based testing with jqwik

---

## 🌐 Demo (Optional, Temporary Public Access)

Use only for short-lived demos. **Do not commit `.env` changes.**

### Setup Demo

1. Start the stack
   ```bash
   docker compose up -d --build
   ```

2. Open tunnels in two separate terminals
   ```bash
   # Terminal 1 - Backend
   cloudflared tunnel --url http://localhost:8080
   
   # Terminal 2 - Frontend
   cloudflared tunnel --url http://localhost:5173
   ```

3. Update `.env` with tunnel URLs
   ```env
   VITE_API_BASE_URL=https://<backend-tunnel-url>
   VITE_ALLOWED_HOSTS=.trycloudflare.com
   CORS_ALLOWED_ORIGIN_PATTERNS=https://*.trycloudflare.com
   ```

4. Rebuild frontend to apply changes
   ```bash
   docker compose up -d --build frontend
   ```

### Stop Demo

```bash
docker compose down
```
Close both tunnel terminals.

---

## 💻 Local Development (Without Docker Compose)

**Prerequisites**: Node 18+, JDK 17, Maven, Docker (for infrastructure)

### 1. Start Infrastructure Only

```bash
docker compose up -d postgres rabbitmq
```

### 2. Start Order Service

```bash
cd order-service
mvn spring-boot:run
```

### 3. Start Kitchen Worker (New Terminal)

```bash
cd kitchen-worker
mvn spring-boot:run
```

### 4. Start Frontend (New Terminal)

```bash
npm install
npm run dev
```

---

## 🐛 Troubleshooting

### Docker Desktop Not Running

```powershell
docker ps
```
If you see an error, start Docker Desktop from the start menu.

### Port Already in Use

```bash
# Stop existing containers
docker compose down

# Windows - Find and kill process
netstat -ano | findstr :8080
taskkill /PID <PID> /F

# Linux/Mac - Kill process
lsof -ti:8080 | xargs kill -9
```

### Connection Errors on Startup

Wait 10-15 seconds after starting containers. Services need time to initialize.

```bash
# Check logs
docker compose logs -f
```

### Frontend Not Connecting to Backend

1. Verify backend is running: http://localhost:8080/menu
2. Check `VITE_API_BASE_URL` in `.env`
3. Verify CORS configuration in backend

### RabbitMQ Not Processing Messages

```bash
# Check RabbitMQ logs
docker compose logs rabbitmq

# Verify queues
docker exec restaurant-rabbitmq rabbitmqctl list_queues

# Check kitchen-worker connection
docker compose logs kitchen-worker
```

### Clean Slate (Reset Everything)

```bash
# Stop and remove everything
docker compose down -v

# Remove images
docker compose down --rmi all

# Rebuild from scratch
docker compose up --build
```

---

## 📁 Repository Structure

```
restaurant-order-system/
├── src/                              # Frontend React
│   ├── api/                          # HTTP calls and contracts
│   ├── components/                   # Reusable components
│   ├── pages/                        # Application pages
│   │   ├── client/                   # Client pages
│   │   └── kitchen/                  # Kitchen pages
│   ├── store/                        # Global state (cart, auth)
│   └── domain/                       # Domain logic
│
├── order-service/                    # Backend Order Service
│   ├── src/main/java/.../orderservice/
│   │   ├── config/                   # Configuration
│   │   ├── controller/               # REST Controllers
│   │   ├── dto/                      # Data Transfer Objects
│   │   ├── entity/                   # JPA Entities
│   │   ├── repository/               # JPA Repositories
│   │   └── service/                  # Business logic
│   └── src/main/resources/
│       ├── db/migration/             # Flyway migrations
│       └── application.yml           # Configuration
│
├── kitchen-worker/                   # Backend Kitchen Worker
│   ├── src/main/java/.../kitchenworker/
│   │   ├── config/                   # RabbitMQ configuration
│   │   ├── entity/                   # JPA Entities
│   │   ├── listener/                 # RabbitMQ listeners
│   │   ├── repository/               # JPA Repositories
│   │   └── service/                  # Business logic
│   └── src/test/                     # Unit tests
│
├── docker-compose.yml                # Full stack orchestration
├── Dockerfile.frontend               # Frontend Dockerfile
├── order-service/Dockerfile          # Order Service Dockerfile
├── kitchen-worker/Dockerfile         # Kitchen Worker Dockerfile
├── .env.example                      # Environment variables template
└── README.md                         # This file
```

---

## 🛠️ Technology Stack

### Frontend
- React 18, TypeScript, Vite
- TailwindCSS, React Router
- TanStack Query (state management)

### Backend
- Spring Boot 3.2.0
- Spring Data JPA, Spring AMQP
- Flyway (database migrations)
- Lombok, SpringDoc OpenAPI (Swagger)

### Infrastructure
- PostgreSQL 15 (database)
- RabbitMQ 3 (message broker)
- Docker & Docker Compose

### Testing
- JUnit 5, Mockito
- jqwik (property-based testing)

---

## 📖 Additional Documentation

- [SISTEMA_FUNCIONANDO.md](SISTEMA_FUNCIONANDO.md) - Complete verification and testing guide
- [AI_WORKFLOW.md](AI_WORKFLOW.md) - AI workflow documentation
- [.kiro/specs/](./kiro/specs/) - Technical specifications

---

## ✨ Key Features

- ✅ Microservices architecture with async communication
- ✅ Modern React frontend with TypeScript
- ✅ Dual interface: Client and Kitchen
- ✅ Real-time event-driven communication
- ✅ Dead Letter Queue for error handling
- ✅ Interactive Swagger documentation
- ✅ Database migrations with Flyway
- ✅ Comprehensive unit tests
- ✅ Property-based testing
- ✅ Robust exception handling
- ✅ Data validation
- ✅ Structured logging
- ✅ Easy deployment with Docker Compose
- ✅ Configurable environment variables

---

## 📝 Notes for Production

- Set `VITE_USE_MOCK=false`
- Configure `VITE_API_BASE_URL` with your real domain
- Set `CORS_ALLOWED_ORIGIN_PATTERNS` to your real domain
- Use strong database credentials
- Enable HTTPS/TLS
- Configure proper logging and monitoring
- Set up backup strategies for PostgreSQL
- Configure RabbitMQ clustering for high availability

---

**Developed with ❤️ using Spring Boot, React, and microservices architecture**

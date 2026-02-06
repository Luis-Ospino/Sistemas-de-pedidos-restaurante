# Sistemas-de-pedidos-restaurante

# Para ejecutar Docker con tu configuración actual, sigue estos pasos:

# 1. Requisitos previos:
# Instala Docker Desktop (incluye Docker y Docker Compose)
# Asegúrate de que el servicio Docker esté corriendo

# 2. Ejecuta los servicios:
# Abre una terminal en la carpeta del proyecto y ejecuta:
# docker-compose up
# O para ejecutar en segundo plano:
# docker-compose up -d

# 3. Verifica que los servicios estén corriendo:
# docker-compose ps

# Services que se levantarán:

# PostgreSQL (puerto 5432): Base de datos orders_db
# RabbitMQ (puertos 5672 y 15672): Message broker
# Panel de administración: http://localhost:15672 (usuario: guest, contraseña: guest)

# Para detener los servicios:
# docker-compose down


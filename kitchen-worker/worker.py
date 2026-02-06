import logging
from celery_app import app

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Iniciando Kitchen Worker...")
    app.worker_main([
        'worker',
        '--loglevel=info',
        '--concurrency=4'
    ])

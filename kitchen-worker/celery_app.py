from celery import Celery
import config

app = Celery('kitchen_worker')

# Configuración de Celery
app.conf.update(
    broker_url=config.CELERY_BROKER_URL,
    result_backend=config.CELERY_RESULT_BACKEND,
    task_serializer=config.CELERY_TASK_SERIALIZER,
    result_serializer=config.CELERY_RESULT_SERIALIZER,
    accept_content=config.CELERY_ACCEPT_CONTENT,
    timezone=config.CELERY_TIMEZONE,
    enable_utc=config.CELERY_ENABLE_UTC,
)

# Auto-discover tasks
app.autodiscover_tasks(['tasks'])

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

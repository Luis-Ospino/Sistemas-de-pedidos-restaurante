from celery_app import app
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@app.task(name='kitchen.process_order')
def process_order(order_id, table_number, items):
    """
    Procesa una orden de cocina
    
    Args:
        order_id: ID de la orden
        table_number: Número de mesa
        items: Lista de items de la orden
    """
    try:
        logger.info(f"Procesando orden {order_id} de la mesa {table_number}")
        logger.info(f"Items: {items}")
        
        # Simular tiempo de preparación
        import time
        time.sleep(2)
        
        logger.info(f"Orden {order_id} procesada correctamente")
        return {
            'order_id': str(order_id),
            'status': 'completed',
            'processed_at': datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error procesando orden {order_id}: {str(e)}")
        return {
            'order_id': str(order_id),
            'status': 'failed',
            'error': str(e)
        }

@app.task(name='kitchen.cancel_order')
def cancel_order(order_id):
    """
    Cancela una orden
    
    Args:
        order_id: ID de la orden a cancelar
    """
    try:
        logger.info(f"Cancelando orden {order_id}")
        return {
            'order_id': str(order_id),
            'status': 'cancelled',
            'cancelled_at': datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error cancelando orden {order_id}: {str(e)}")
        return {
            'order_id': str(order_id),
            'status': 'failed',
            'error': str(e)
        }

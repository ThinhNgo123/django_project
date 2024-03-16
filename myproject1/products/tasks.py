# ce/taks.py
# Create your tasks here
from celery import shared_task
from myproject1 import celery_app
from myproject1.celery import logger
from .models import Product

@shared_task
def debug_task():
    # logger.info("-"*25)
    print("-"*25)
    print(Product.objects.values())
    # logger.info("Printing Hello from Celery")
    print("-"*25)
    # logger.info("-"*25)
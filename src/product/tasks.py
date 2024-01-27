import time


from celery import shared_task


@shared_task
def mine_bitcoin():
    time.sleep(60)


@shared_task
def generate_products(count):
    count = 5



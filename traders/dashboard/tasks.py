from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random
from decimal import Decimal
from django.utils import timezone
from .models import Trader, Transaction

@shared_task
def do():
    traders = Trader.objects.all()
    for trader in traders:
        amount = random.uniform(-10, 10)
        decimal_amount = Decimal(str(amount))
        new_balance = Decimal(str(trader.balance)) + decimal_amount
        trader.balance = str(new_balance)
        trader.save()
        Transaction.objects.create(trader=trader, amount=decimal_amount, timestamp=timezone.now())

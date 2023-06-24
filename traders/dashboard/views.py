from django.shortcuts import render
from decimal import Decimal
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Trader, Transaction
import json
from decimal import Decimal

from rest_framework.views import APIView

def user_dashboard(request):
    trader = Trader.objects.get(id='2') # the id of each of the 10 traders can be inserted here
    transactions = Transaction.objects.filter(trader=trader)
    balance = trader.balance
    name = trader.name

    # Convert datetime objects to strings
    x_values = [t.timestamp.strftime('%Y-%m-%d %H:%M:%S') for t in transactions]
    y_values = [float(str(t.amount)) for t in transactions]


    x_values_json = json.dumps(x_values)
    y_values_json = json.dumps(y_values)

    return render(request, 'user_dashboard.html', {'x_values_json': x_values_json, 'y_values_json': y_values_json, 'balance': balance, 'name':name})




class AdminDashboardAPIView(APIView):
    def get(self, request):
        traders = Trader.objects.all()
        data = []

        for trader in traders:
            transactions = Transaction.objects.filter(trader=trader)

            # Calculate profit and loss for each trader
            profit = sum(t.amount.to_decimal() for t in transactions if t.amount.to_decimal() > Decimal('0'))
            loss = sum(t.amount.to_decimal() for t in transactions if t.amount.to_decimal() < Decimal('0'))

            # Calculate the current balance of each trader
            balance = trader.balance.to_decimal() + sum(t.amount.to_decimal() for t in transactions)

            data.append({'trader': trader.name, 'transactions': transactions, 'profit': profit, 'loss': loss, 'balance': balance})

        return render(request, 'admin_dashboard.html', {'traders': data})

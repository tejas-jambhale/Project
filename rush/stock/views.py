from django.shortcuts import render

# Create your views here.
from .models import Stocks,Team

def stock_list(request):
    Stock = Stocks.objects.all()

    teams = Team.objects.filter(display='True')

    stockrecent = Stocks.objects.filter(updated='True')
    return render(request, 'stockabc.html', {'Stock': Stock, 'teams1':teams[0:3],'teams2':teams[3:6],'stockrecent':stockrecent})
from django.shortcuts import render

# Create your views here.
from .models import Stocks,Team

def stock_list(request):
    Stock = Stocks.objects.all()
    Stock1 = Stocks.objects.order_by('ticker')

    teams1=Team.objects.filter(display='True').filter(change__gt=0.0)
    teams = Team.objects.filter(display='True').filter(change__lt=0.0)

    stockrecent = Stocks.objects.filter(updated='True').filter(change__gt=0.0)
    stockrecent1= Stocks.objects.filter(updated='True').filter(change__lt=0.0)

    #stockrecent = Stocks.objects.filter(change__gt=0.0)
    #stockrecent1= Stocks.objects.filter(change__lt=0.0)
    
    return render(request, 'stockabc.html', {'Stock': Stock,'Stock1':Stock1, 'teams1':teams1[0:3],'teams':teams[0:3],'stockrecent':stockrecent[0:7],'stockrecent1':stockrecent1[0:7],'stockrecent2':stockrecent[3:10],'stockrecent3':stockrecent1[3:10]})
    #return render(request, 'stockabc.html', {'Stock': Stock,'Stock1':Stock1, 'teams1':teams[0:3],'teams2':teams[3:6],'stockrecent':zip(stockrecent[0:7],stockrecent1[0:7])})
from django.db import models

# Create your models here.
class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 10,null='true',blank='true')
    ticker = models.CharField(max_length = 10)
    currentprice = models.FloatField()
    change = models.FloatField()
    lastprice = models.FloatField()
    updated = models.BooleanField(default='False',null='true')
    percent = models.FloatField(null='true',blank='true')
    marketcap = models.FloatField(null='true',blank='true')

    def __str__(self):
        return self.ticker    

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    balance = models.FloatField()
    change = models.FloatField()
    display = models.BooleanField(default='False',null='true')

    def __str__(self):
        return self.name
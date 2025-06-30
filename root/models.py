from django.db import models


class NbuCurrency(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sname = models.CharField(max_length=3)
    fname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'nbu_currency'
        app_label = 'nbu'


class NbuRate(models.Model):
    currencyid = models.ForeignKey(NbuCurrency, models.DO_NOTHING, db_column='currencyid', primary_key=True)
    rate = models.FloatField()
    fromdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'nbu_rate'
        unique_together = (('currencyid', 'fromdate'),)
        app_label = 'nbu'
        
class Vdjrate(models.Model):
    fromdate = models.DateField(primary_key=True)
    usd = models.FloatField()
    eur = models.FloatField()

    class Meta:
        managed = False
        db_table = 'vdjrate'
        app_label = 'nbu'


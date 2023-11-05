from django.db import models


# Create your models here.
class Algo(models.Model):
    uid = models.AutoField(verbose_name="Идентификатор", primary_key=True)
    res = models.TextField(blank=True, verbose_name="Результат")
    number_A = models.FloatField(verbose_name="A", default=0)
    number_B = models.FloatField(verbose_name="B", default=0)
    number_C = models.FloatField(verbose_name="C", default=0)

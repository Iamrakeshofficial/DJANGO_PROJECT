from django.db import models

class Product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=20)
    price = models.FloatField()
    rating = models.IntegerField()
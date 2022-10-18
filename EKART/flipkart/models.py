from django.db import models

class Product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=20)
    price = models.FloatField()
    rating = models.IntegerField()
# Create your models here.
class Customer(models.Model):
    customer_name=models.CharField(max_length=25)
    customer_id=models.IntegerField()
    customer_email=models.EmailField(max_length=25)
    customer_phono=models.IntegerField()
    customer_addrs=models.TextField(max_length=75)



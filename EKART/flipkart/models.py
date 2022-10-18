from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name=models.CharField(max_length=25)
    customer_id=models.IntegerField()
    customer_email=models.EmailField(max_length=25)
    customer_phono=models.IntegerField()
    customer_addrs=models.TextField(max_length=75)



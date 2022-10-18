from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','customer_name','customer_id','customer_email','customer_phono','customer_addrs']

from django.shortcuts import render,HttpResponse
from .models import Customer
from .forms import User

# Create your views here.
def show(request):
    if request.method=='POST':
        fm=User(request.POST)
        if fm.is_valid():
            cn=fm.cleaned_data['customer_name']
            ci=fm.cleaned_data['customer_id']
            ce=fm.cleaned_data['customer_email']
            cp=fm.cleaned_data['customer_phono']
            ca=fm.cleaned_data['customer_addrs']
        reg=Customer(customer_name=cn,customer_id=ci,customer_email=ce,customer_phono=cp,customer_addrs=ca)
        reg.save()
        fm=User()


    else:
        fm=User()








    return render(request,'contact.html',{'form':fm})

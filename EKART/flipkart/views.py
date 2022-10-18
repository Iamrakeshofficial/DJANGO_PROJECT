from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductInformation
from .models import Product
# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        pri = ProductInformation(request.POST)
        if pri.is_valid():
            pd = pri.cleaned_data['pid']
            pn = pri.cleaned_data['pname']
            pr = pri.cleaned_data['price']
            rt = pri.cleaned_data['rating']
            reg = Product(pid = pd, pname=pn, price = pr, rating = rt)
            reg.save()
            pri = ProductInformation()
    else:
        pri = ProductInformation()
    ob = Product.objects.all()
    return render(request, 'addnshow_details.html', {'form':pri, 'ob':ob})

# This Function will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pri = ProductInformation(request.POST, instance=pi)
        if pri.is_valid():
            pri.save()
    else:
        pi = Product.objects.get(pk=id)
        pri = ProductInformation(instance=pi)
    return render(request, 'update_details.html', {'form': pri})

# This Function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
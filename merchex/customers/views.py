from django.shortcuts import render, redirect
from django.http import HttpResponse
from customers.models import Customer
from .forms import CustomerForm

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer/home.html', context)

def show(request, pk):
    custom = Customer.objects.get(id = pk)
    context = {'custom': custom}
    return render(request, 'customer/show.html', context)

def addcustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'customer/add_customer.html', context)

def updatecustomer(request,pk):
    customer = Customer.objects.get(id = pk)
    form = CustomerForm(instance = customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'customer/add_customer.html', context)

def deletecustomer(request, pk):
    customer = Customer.objects.get(id = pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'item': customer}
    return render(request, 'customer/delete_customer.html', context)
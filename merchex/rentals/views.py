from django.shortcuts import render, redirect
from django.http import HttpResponse
from rentals.models import Rental
from .forms import RentalForm

# Create your views here.

def addrental(request):
    form = RentalForm()
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'rental/add_rental.html', context)

def updaterental(request,pk):
    rental = Rental.objects.get(id = pk)
    form = RentalForm(instance = rental)
    if request.method == 'POST':
        form = RentalForm(request.POST, instance = rental)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'rental/add_rental.html', context)

def deleterental(request, pk):
    rental = Rental.objects.get(id = pk)
    if request.method == 'POST':
        rental.delete()
        return redirect('/')
    context = {'item': rental}
    return render(request, 'rental/delete_rental.html', context)

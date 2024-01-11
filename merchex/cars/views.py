from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from .forms import CarForm


# Create your views here.
def list_car(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'car/car.html', context)

def show(request, pk):
    car = Car.objects.get(id = pk)
    context = {'car': car}
    return render(request, 'car/show.html', context)

def addcar(request):
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars/cars')
    context = {'form': form}
    return render(request, 'car/add_car.html', context)

def updatecar(request,pk):
    car = Car.objects.get(id = pk)
    form = CarForm(instance = car)
    if request.method == 'POST':
        form = CarForm(request.POST, instance = car)
        if form.is_valid():
            form.save()
            return redirect('/cars/cars')
    context = {'form': form}
    return render(request, 'car/add_car.html', context)

def deletecar(request, pk):
    car = Car.objects.get(id = pk)
    if request.method == 'POST':
        car.delete()
        return redirect('/cars/cars')
    context = {'item': car}
    return render(request, 'car/delete_car.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm
from categories.models import Category

# Create your views here.

def categorylist(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/category_list.html', context)

def addcategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars/cars')
    context = {'form': form}
    return render(request, 'category/add_category.html', context)

def updatecategory(request,pk):
    category = Category.objects.get(id = pk)
    form = CategoryForm(instance = category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('/categories/category_list')
    context = {'form': form}
    return render(request, 'category/add_category.html', context)

def deletecategory(request, pk):
    category = Category.objects.get(id = pk)
    if request.method == 'POST':
        category.delete()
        return redirect('/categories/category_list')
    context = {'item': category}
    return render(request, 'category/delete_category.html', context)

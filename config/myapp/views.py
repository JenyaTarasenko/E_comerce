from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Product
def index(request):
    """"first page"""
    item = Product.objects.all()
    return render(request, 'myapp/index.html', {'item': item})


class ProductListView(ListView):
    """
    First page class ListView
    """
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'item'#object list in templates



def index_item(request, id):
    """"detail page"""
    item = Product.objects.get(id=id)
    return render(request, 'myapp/detail.html', {'item': item})


class DetailListView(DetailView):
    """"detail page class DetailView """
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = 'item'


def add(request):
    """"form page add product"""
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES['upload']
        item = Product(name=name, price=price, description=description, image=image)#связанная с моделью
        item.save()#сохраняем
    return render(request, 'myapp/additem.html')



def updaitem(request, id):
    """"form page update product"""
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.description = request.POST.get('description')
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect('/')
    return render(request, 'myapp/updateitem.html', {'item': item})



def delete_item(request, id):
    """"form page delete product"""
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, 'myapp/deleteitem.html', {'item': item})
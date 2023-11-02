from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .models import Product
from django.core.paginator import Paginator


def index(request):
    """"first page"""
    item = Product.objects.all()
    paginator = Paginator(item, 2)#пагинация без класса
    page_number = request.GET('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/index.html', {'item': item, 'page_obj': page_obj})


class ProductListView(ListView):
    """
    First page class ListView
    """
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'item'#object list in templates
    paginate_by = 2 #для пагинации передается page_obj



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



class ProductDeleteView(DeleteView):
    """"form page delete product"""
    model = Product
    success_url = reverse_lazy('myapp:index')#переопределяем на главную страничку




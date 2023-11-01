from django.urls import path
from . import views



app_name ='myapp'

urlpatterns = [
    # path('', views.index, name='index'),#first page
    path('', views.ProductListView.as_view(), name='index'), #class ListView
    # path('product/<int:id>/', views.index_item, name='detail'),#add page
    path('product/<int:pk>/', views.DetailListView.as_view(), name='detail'),#class DetailView
    path('additem/', views.add, name='add_item'),
    path('updaitem/<int:id>', views.updaitem, name='up_item'),
    path('deleteitem/<int:id>', views.delete_item, name='del_item')
]
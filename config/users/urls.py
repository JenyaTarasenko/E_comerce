from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView



app_name ='users'

urlpatterns = [
    path('register/', views.register, name='register'),#регистрация
    #функция работает без views сразу template_name='users/login.html
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),#перенапрвление зарегестрированного пользователя

]
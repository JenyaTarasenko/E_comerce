from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login

def register(request):
    """форма регистрации юзера"""
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('myapp:index')
    form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})



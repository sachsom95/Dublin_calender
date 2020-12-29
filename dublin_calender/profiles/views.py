from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'profiles/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created {username} woop woop!")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'profiles/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from scheduling.models import WorkShift
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            try:
                user_profile = user.profile
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user)
            return redirect(reverse('profiles:profile_detail'))
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                user_profile = user.profile
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user)
            return redirect(reverse('profiles:profile_detail'))
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'authentication/login.html')


def user_logout(request):
    logout(request)
    return redirect('authentication:login')

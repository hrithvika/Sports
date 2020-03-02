from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate
# Create your views here.


def register(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get('')
        user.email = request.POST.get('')
        user.password = request.POST.get('')
        profile = Profile()
        profile.user = user
        profile.game = request.POST.get('')
        profile.gender = request.POST.get('')
        profile.age = request.POST.get('')
        profile.save()
        return render(request, '#')
    else:
        return render(request, '#')


def login(request):
    if request.method == "POST":
        email = request.POST.get('')
        password = request.POST.get('')
        user = authenticate(email=email, password=password)
        if user is not None:
            return redirect('app1:home.html')
        else:
            return redirect('app1:login.html')


def booking(request, game_id):
    game = Game.objects.get(pk=game_id)
    template = 'app1:bookings.html'
    return render(request, template)


def ad(request):
    template = 'app1/advertisement.html'
    ad = request.POST.get('advertisement ')
    return render(request, template)



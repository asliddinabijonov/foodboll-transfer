from django.shortcuts import render, redirect
from .models import  *
from django.views import View
class Home(View):
    def get(self, request):
        return render(request, 'index.html')

class About(View):
    def get(self, request):
        return render(request, 'about.html')

class Tryouts(View):
    def get(self, request):
        return render(request, 'tryouts.html')

class Clubs(View):
    def get(self, request):
        context = {
            'clublar': Club.objects.order_by('-kapital')
        }
        return render(request, 'clubs.html', context)

class Players(View):
    def get(self, request):
        context = {
            'players': Player.objects.order_by('ism')
        }
        return render(request, 'players.html', context)

class U20(View):
    def get(self, request):
        context = {
            'u20': Player.objects.order_by('-narx').filter(t_sana__gt='2004-01-01')
        }
        return render(request, "U-20 players.html", context)


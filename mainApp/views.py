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


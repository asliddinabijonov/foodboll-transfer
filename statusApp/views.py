from django.shortcuts import render
from django.views import View
from .models import *


class Latest(View):
    def get(self, request):
        context = {
            'transferlar': Transfer.objects.order_by("-sana")
        }
        return render(request, 'latest-transfers.html', context)


class Stats(View):
    def get(self, request):
        return render(request, 'stats.html')


class Records(View):
    def get(self, request):
        context = {
            'transferlar': Transfer.objects.order_by("-narx")
        }
        return render(request, 'transfer-records.html', context)


class Predictions(View):
    def get(self, request):
        context = {
            'transfers': Transfer.objects.order_by('-taxmin_narx')
        }
        return render(request, 'stats/150-accurate-predictions.html', context)


class Expenditure(View):
    def get(self, request):
        return render(request, 'stats/top-50-clubs-by-expenditure-in-2021.html')


class Income(View):
    def get(self, request):
        return render(request, 'stats/top-50-clubs-by-income-in-2021.html')

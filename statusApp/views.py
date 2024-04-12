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

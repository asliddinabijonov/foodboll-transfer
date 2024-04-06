from django.shortcuts import render
from django.views import View
from .models import *

class Latest(View):
    def get(self, request):
        context = {
            'transferlar': Transfer.objects.order_by("-sana")
        }
        return render(request, 'latest-transfers.html', context )

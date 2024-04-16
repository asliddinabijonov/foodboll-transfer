from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *
from statusApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('tryouts/', Tryouts.as_view(), name='tryouts'),
    path('clubs/', Clubs.as_view(), name='club'),
    path('clubs/<int:pk>/', Oyinchilar.as_view(), name='oyinchilar'),
    path('latest/', Latest.as_view(), name='latest'),
    path('players/', Players.as_view(), name='players'),
    path('u20/', U20.as_view(), name='u20'),
    path('davlatlar/<int:pk>/clubs/', CountryClubs.as_view(), name='country-clubs'),
    path('stats/', Stats.as_view(), name='stats'),
    path('stats/records/', Records.as_view(), name='records'),
    path('stats/predictions/', Predictions.as_view(), name='predictions'),
    path('stats/expenditure/', Expenditure.as_view(), name='predictions'),
    path('stats/income/', Income.as_view(), name='predictions'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

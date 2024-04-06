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
    path('latest/', Latest.as_view(), name='latest')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

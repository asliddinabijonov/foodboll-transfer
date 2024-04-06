from django.contrib import admin
from .models import *
admin.site.register([Davlat, Pozitsiya])

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    search_fields = ("nom", )
    list_filter = ("davlat", )

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ("ism", )
    list_filter = ("club", )
    autocomplete_fields = ("club", )
from django.contrib import admin
from .models import Aspirant, FairRegistration, FairFavorite

@admin.register(Aspirant)
class AspirantAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'secondName', 'lastName', 'phone')
    search_fields = ('lastName', 'email')

@admin.register(FairRegistration)
class FairRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'aspirant', 'fair', 'registrationDate')
    search_fields = ('aspirant', 'fair')

@admin.register(FairFavorite)
class FairFavorite(admin.ModelAdmin):
    list_display = ('id', 'aspirant', 'fair', 'favoriteDate')
    search_fields = ('aspirant', 'fair')

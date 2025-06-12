from django.contrib import admin
from .models import Cake

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer_price')

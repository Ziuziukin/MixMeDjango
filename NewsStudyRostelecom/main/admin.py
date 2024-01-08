from django.contrib import admin
from .models import *

class BrandsAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'site_brand', 'brand_author']
    list_filter = ['brand_name', 'brand_author']

admin.site.register(Brands, BrandsAdmin)

class TastesAdmin(admin.ModelAdmin):
    list_display = ['name_taste', 'taste_rus', 'taste_image', 'strength_taste']
    list_filter = ['name_taste', 'taste_rus', 'strength_taste']

admin.site.register(Tastes, TastesAdmin)
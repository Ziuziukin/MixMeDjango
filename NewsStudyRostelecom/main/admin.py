from django.contrib import admin
from .models import *

class BrandsAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'site_brand', 'brand_author']

admin.site.register(Brands, BrandsAdmin)
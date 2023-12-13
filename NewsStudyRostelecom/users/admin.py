from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'birthdate', 'account_image']
    list_filter = ['user', 'birthdate']

admin.site.register(Account, AccountAdmin)
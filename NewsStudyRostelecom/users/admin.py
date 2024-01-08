from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'birthdate', 'get_account_image']
    list_filter = ['user', 'birthdate']

    def get_account_image(self, obj):
        return mark_safe(f'<img src={obj.account_image.url} width="50px", height="auto"')

    get_account_image.shrt_description = 'Изображение'

admin.site.register(Account, AccountAdmin)

class Favorite_TasteAccountAdmin(admin.ModelAdmin):
    list_display = ['user_id_favorite', 'taste_id_favorite', 'favorite_choices']

admin.site.register(Favorite_Taste, Favorite_TasteAccountAdmin)
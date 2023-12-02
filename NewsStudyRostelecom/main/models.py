from django.db import models
from django.contrib.auth.models import User

#Модель для брендов
class Brands(models.Model):
    brand_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand_name = models.CharField('Название бренда', max_length=70, default='')
    desc_brand = models.TextField('Описание бренда', max_length=2000)
    site_brand = models.TextField('Сайт бренда', max_length=50)

    def __str__(self):
        return self.brand_name

    def get_absolute_url(self):
        return self.brand_name
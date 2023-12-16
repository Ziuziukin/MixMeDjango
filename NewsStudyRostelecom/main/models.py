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

    class Meta:
        ordering = ['brand_name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'



#добавление тегов - 2:01:52, урок 7
#оптимизация запросов - урок 8
#формы django - урок 9
#дженерики - урок 10
#несколько картинок к одной записи в бд - урок 11
#регистрация и авторизация пользователей - урок 12





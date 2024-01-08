from django.db import models
from django.contrib.auth.models import User

#Модель для брендов
class Brands(models.Model):
    brand_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    brand_name = models.CharField('Название бренда', max_length=70, default='')
    desc_brand = models.TextField('Описание бренда', max_length=2000, default='')
    site_brand = models.TextField('Сайт бренда', max_length=50)
    brand_image = models.ImageField(default='brands_images/default_brand.jpg', upload_to='brands_images')

    def __str__(self):
        return self.brand_name

    class Meta:
        ordering = ['brand_name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

#Модель для вкусов
class Tastes(models.Model):
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE, default='')
    name_taste = models.CharField('Название вкуса', max_length=90, default='')
    taste_rus = models.CharField('Русское название вкуса', max_length=90, default='')
    desc_taste = models.TextField('Описание вкуса', max_length=2000)
    taste_image = models.ImageField(default='tastes_images/default_taste.jpg', upload_to='tastes_images')
    strength_taste = models.IntegerField('Крепость вкуса')

    def __str__(self):
        return self.name_taste

    class Meta:
        ordering = ['name_taste']
        verbose_name = 'Вкус'
        verbose_name_plural = 'Вкусы'


#добавление тегов - 2:01:52, урок 7
#оптимизация запросов, джанго тул бар консоль - урок 8
#формы django - урок 9
#дженерики - урок 10
#несколько картинок к одной записи в бд - урок 11
#регистрация и авторизация пользователей - урок 12





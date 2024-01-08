from django.db import models
from django.contrib.auth.models import User

from main.models import Tastes


class Account(models.Model):
    gender_choices = (('М', 'Мужской'),
                      ('Ж', 'Женский'),
                      ('НД', 'Нет данных'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices, max_length=20)
    account_image = models.ImageField(default='account_images/default_user.jpg', upload_to='account_images')

    def __str__(self):
        return f"{self.user.username}'s account"

class Favorite_Taste(models.Model):
    user_id_favorite = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    taste_id_favorite = models.ForeignKey(Tastes, on_delete=models.CASCADE, default='')
    favorite_choices = models.BooleanField()

    class Meta:
        unique_together = ('user_id_favorite', 'taste_id_favorite')
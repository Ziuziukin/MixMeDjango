from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    gender_choices = (('М', 'Мужской'),
                      ('Ж', 'Женский'),
                      ('НД', 'Нет данных'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices, max_length=20)
    account_image = models.ImageField(default='default_user.png', upload_to='account_images')

    def __str__(self):
        return f"{self.user.username}'s account"
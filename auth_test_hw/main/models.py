from django.db import models
import re
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField('Телефон', max_length=20, blank=True)
    address = models.TextField('Адрес', blank=True)

    def clean(self):
        if self.telephone and not re.match(r'^\+?[0-9]{7,15}$', self.telephone):
            raise ValidationError({'telephone': 'Введите корректный номер телефона'})

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



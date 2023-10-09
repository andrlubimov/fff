from django.db import models


# Create your models here.
class uslugi(models.Model):
    title = models.TextField(max_length=20),
    name = models.TextField(max_length=20, verbose_name='заголовок')
    body = models.TextField(max_length=60, verbose_name='сообщение')


from django.db import models
import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    imagen = models.ImageField(upload_to='blog/imagen')
    date = models.DateField(datetime.date.today)

from django.db import models
import datetime

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=999)
    imagen = models.ImageField(upload_to='blog/imagen')
    date = models.DateField(datetime.date.today)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='blog/imagen')
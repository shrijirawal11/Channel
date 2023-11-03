from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class writer(models.Model):
    name = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class post(models.Model):
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    writer=models.ForeignKey(writer,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='null')
     

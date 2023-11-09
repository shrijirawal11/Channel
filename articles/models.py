from django.db import models

# Create your models here.
class post(models.Model):
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
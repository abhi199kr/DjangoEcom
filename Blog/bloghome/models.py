from turtle import title
from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)
    slug=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

from django.db import models
from django.forms import CharField

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
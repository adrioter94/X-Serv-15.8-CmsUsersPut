from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=32)
    page = models.TextField()
    
# Create your models here.

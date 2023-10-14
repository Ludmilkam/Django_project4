from django.db import models

# Create your models here.
class Games(models.Model):
    game = models.CharField(max_length=255)
    price = models.IntegerField()
    creator = models.TextField()
    year = models.CharField(max_length=255)

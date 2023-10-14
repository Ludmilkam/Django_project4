from django.db import models

# Create your models here.
class Games(models.Model):
    usernames = models.CharField(max_length=255)
    amount_money = models.IntegerField()
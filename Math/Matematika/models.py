from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Korisnik(models.Model):
    korisnik=models.ForeignKey(User, on_delete=models.CASCADE)
    nivo=models.IntegerField()

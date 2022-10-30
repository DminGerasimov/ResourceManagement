from django.db import models

class User(models.Model):
  name = models.CharField(max_length=30,)
  login = models.CharField(max_length=30, unique=True)
  phone = models.CharField(max_length=12, unique=True)
  password = models.CharField(max_length=200)
  birth = models.DateField(auto_now=False, auto_now_add=False)
  tg = models.CharField(max_length=20)
  email = models.EmailField(max_length=254)

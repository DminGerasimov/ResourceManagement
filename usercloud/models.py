from django.db import models


class User(models.Model):
  phone = models.CharField(max_length=12)
  login = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=200)
  name = models.CharField(max_length=30,)
  birth = models.DateField(auto_now=False, auto_now_add=False)
  tg = models.CharField(max_length=20, blank=True)
  email = models.EmailField(max_length=254, blank=True)


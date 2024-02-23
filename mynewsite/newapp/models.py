from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=25, unique=True)
    hidden_field = models.CharField(max_length=4)
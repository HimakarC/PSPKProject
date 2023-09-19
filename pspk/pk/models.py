from django.db import models

# Create your models here.

class reg(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    password = models.CharField(max_length=100)
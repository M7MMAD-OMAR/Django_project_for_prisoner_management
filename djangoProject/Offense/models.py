from django.db import models


# Create your models here.

class Offense(models.Model):
    name = models.CharField(max_length=50, null=False)

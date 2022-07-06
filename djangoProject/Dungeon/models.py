from django.db import models

# Create your models here.

class Dungeon(models.Model):
    name = models.DateField(max_length=50, null=False)
    size = models.IntegerField(null=False)




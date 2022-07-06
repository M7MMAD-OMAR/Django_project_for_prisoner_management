from django.db import models


# Create your models here.

class Dungeon_Moves(models.Model):
    dungeon_id = models.IntegerField(null=False)
    person_id = models.IntegerField(null=False)
    from_date = models.DateField(null=False)

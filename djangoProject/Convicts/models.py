from django.db import models


# Create your models here.
class Convicts(models.Model):
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)
    person_id = models.IntegerField(null=False)
    offense_id = models.IntegerField(null=False)

from django.db import models

# Create your models here.

class Visits(models.Model):
    date_visited = models.DateField(null=False)
    person_id = models.IntegerField(null=False)
    visitor_name = models.CharField(max_length=50, null=False)
    mount_in_minutes = models.IntegerField(null=False)

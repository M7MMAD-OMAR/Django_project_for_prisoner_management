from django.db import models


# Create your models here.


class Person(models.Model):
    SEMESTER_CHOICES = (("male", "male"), ("female", "female"))
    first_name = models.CharField(max_length=50, null=False)
    father = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default='1')
    birth_year = models.DateField(null=False)
    address = models.TextField(max_length=100, null=False)

    def __str__(self):
        return self.first_name

    # def __unicode__(self):
    #     return self.father

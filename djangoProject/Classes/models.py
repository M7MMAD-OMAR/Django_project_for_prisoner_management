from django.db import models


# Create your models here.


class Person(models.Model):
    person_id = models.AutoField(primary_key=True, blank=True, unique=True)
    SEMESTER_CHOICES = (("male", "male"), ("female", "female"))
    first_name = models.CharField(max_length=50, null=False, verbose_name="first name")
    father = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default='1')
    birth_year = models.DateField(null=False, blank=True)
    address = models.TextField(max_length=100, null=False)

    def __str__(self):
        return f"{str(self.person_id)}, {self.first_name}"


class Offense(models.Model):
    offense_id = models.AutoField(primary_key=True, blank=True, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{str(self.offense_id)}, {self.name}"


class Dungeon(models.Model):
    dungeon_id = models.AutoField(primary_key=True, blank=True, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True)
    size = models.BigIntegerField(null=False)

    def __str__(self):
        return f"{str(self.dungeon_id)}, {self.name}"


class Visits(models.Model):
    visits_id = models.AutoField(primary_key=True, blank=True, unique=True)
    date_visited = models.DateField(null=False)
    person_id = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Person ID",
    )
    visitor_name = models.CharField(max_length=50, null=False)
    mount_in_minutes = models.TimeField(null=False)

    def __str__(self):
        return f"{str(self.visits_id)}, {self.visitor_name}"


class Convicts(models.Model):
    convicts_id = models.AutoField(primary_key=True, blank=True, unique=True)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)
    person_id = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Person ID",
    )
    offense_id = models.ForeignKey(
        Offense,
        on_delete=models.CASCADE,
        verbose_name="Offense ID",
    )

    def __str__(self):
        return f"{str(self.convicts_id)}"


class Dungeon_Moves(models.Model):
    dungeon_moves_id = models.AutoField(primary_key=True, blank=True, unique=True)
    person_id = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Person ID",
    )
    dungeon_id = models.ForeignKey(
        Dungeon,
        on_delete=models.CASCADE,
        verbose_name="Dungeon ID",
    )
    from_date = models.DateField(null=False)

    def __str__(self):
        return f"{str(self.dungeon_moves_id)}"

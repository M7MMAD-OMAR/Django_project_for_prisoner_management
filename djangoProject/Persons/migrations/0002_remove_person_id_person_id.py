# Generated by Django 4.0.5 on 2022-07-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AddField(
            model_name='person',
            name='Id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

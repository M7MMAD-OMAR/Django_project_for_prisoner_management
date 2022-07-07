# Generated by Django 4.0.5 on 2022-07-06 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convicts',
            name='Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.offense', verbose_name='the related Offense'),
        ),
        migrations.AlterField(
            model_name='dungeon_moves',
            name='Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.dungeon', verbose_name='the related Dungeon'),
        ),
        migrations.AlterField(
            model_name='visits',
            name='mount_in_minutes',
            field=models.TimeField(),
        ),
    ]
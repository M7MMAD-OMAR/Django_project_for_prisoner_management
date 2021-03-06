# Generated by Django 4.0.5 on 2022-07-06 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.DateField(max_length=50)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offense',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('father', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='1', max_length=10)),
                ('birth_year', models.DateField()),
                ('address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visited', models.DateField()),
                ('visitor_name', models.CharField(max_length=50)),
                ('mount_in_minutes', models.IntegerField()),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.person', verbose_name='the related Person')),
            ],
        ),
        migrations.CreateModel(
            name='Dungeon_Moves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.person', verbose_name='the related Person')),
            ],
        ),
        migrations.CreateModel(
            name='Convicts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.person', verbose_name='the related Person')),
            ],
        ),
    ]

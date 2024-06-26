# Generated by Django 4.2 on 2024-04-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('running_time', models.TimeField()),
                ('director', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField()),
                ('actors', models.ManyToManyField(to='shoes.actor')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

from django.db import models

# Create your models here.

class Actor(models.Model):
    # PK id created by default id (bigint), you may override that with th e
    # following line
    # id = models.SmallIntegerField(auto_increment=True, primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50, unique=True)
    running_time = models.TimeField()
    actors = models.ManyToManyField(Actor)
    director = models.CharField(max_length=200)
    release_date = models.DateTimeField()

    class Meta:
        ordering = ['name']

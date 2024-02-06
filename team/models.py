from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    members = models.ManyToManyField('Member', related_name='teams', blank=True)

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

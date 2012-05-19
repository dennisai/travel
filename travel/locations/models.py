from django.db import models

class Relevance(models.Model):
    concept = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    relevance = models.IntegerField()
    explanation = models.TextField()

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField()

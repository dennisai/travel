from django.db import models

class Relevance(models.Model):
    concept = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    relevance = models.IntegerField()
    explanation = models.TextField()

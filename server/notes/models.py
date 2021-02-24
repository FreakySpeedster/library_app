from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=500, blank=True)
    topic = models.CharField(max_length=500, blank=True)
    content = models.TextField(blank=True)
    labels = TaggableManager(blank=True)

    def __str__(self):
        return self.title

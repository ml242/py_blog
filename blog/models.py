from django.db import models

# Create your models here.

class posts(models.Model):
  author = models.Charfield(max_length = 30)
  title = models.Charfield(max_length = 100)
  bodytext = models.TextField()
  timestamp = models.DateTimeField()
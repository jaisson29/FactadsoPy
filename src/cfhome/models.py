from django.db import models
from django.contrib.auth.models import User

class producto (models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField(blank=True)
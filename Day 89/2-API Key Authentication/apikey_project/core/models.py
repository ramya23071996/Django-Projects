
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, default="Viewer")

class Project(models.Model):
    name = models.CharField(max_length=100)

class ProjectAPIKey(AbstractAPIKey):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
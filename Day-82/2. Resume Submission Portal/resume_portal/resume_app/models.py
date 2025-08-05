from django.db import models
import os

def resume_upload_path(instance, filename):
    return os.path.join('resumes', filename)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to=resume_upload_path)

    def __str__(self):
        return f"{self.name} - {self.position}"
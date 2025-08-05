from django.db import models
import uuid
import os

def unique_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('photos', filename)

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    student_id = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to=unique_photo_path)

    def __str__(self):
        return f"{self.name} ({self.student_id})"
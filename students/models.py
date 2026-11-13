from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    course = models.CharField(max_length=100)

    marks = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UploadedDocument(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
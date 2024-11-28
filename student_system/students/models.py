from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return self.name


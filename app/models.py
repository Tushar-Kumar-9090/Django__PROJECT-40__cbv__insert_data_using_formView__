from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_name
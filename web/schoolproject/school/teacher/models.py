from django.db import models

class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    teacher_id = models.SmallIntegerField()
    date_of_joining = models.DateField()
    nationality = models.CharField(max_length=20)
    bio = models.TextField()
    years_of_experience = models.SmallIntegerField()
    photo = models.ImageField()

# Create your models here.

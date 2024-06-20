from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    parent = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_id = models.CharField(max_length=20, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    current_enrollment = models.PositiveIntegerField(default=0)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f"{self.class_name} ({self.class_id})"
    
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    credits = models.PositiveSmallIntegerField()
    department = models.CharField(max_length=50)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    is_active = models.BooleanField(default=True)
    level = models.CharField(max_length=20)
    syllabus = models.FileField(upload_to='syllabi/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.course_name} ({self.course_code})"
    
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    teacher_id = models.CharField(max_length=20, unique=True)
    date_of_joining = models.DateField()
    department = models.CharField(max_length=50)
    nationallity = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    education_level = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.

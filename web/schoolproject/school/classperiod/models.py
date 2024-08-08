from django.db import models
from student.models import Student


class ClassPeriod(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.ForeignKey('classes.classes', on_delete=models.CASCADE, related_name='class_periods')
    teacher = models.CharField(max_length=20)
    # teacher = models.ForeignKey( 'teacher.Teacher', on_delete=models.CASCADE, related_name='class_periods')
    students = models.ManyToManyField('student.Student', related_name='class_periods')
    attendance_count = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    capacity = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.title} - ({self.date})"
# Create your models here.

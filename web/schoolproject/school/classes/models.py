from django.db import models

from django.db import models
class Classes(models.Model):
    class_id = models.PositiveSmallIntegerField(primary_key=True)
    room_number = models.CharField(max_length=20)
    teacher_allocated = models.CharField(max_length=20)
    course_tought = models.CharField(max_length=20)
    course_start_time = models.TimeField()
    course_end_time = models.TimeField()
    course_day_of_week = models.CharField(max_length=20)
    seating_arrangement = models.TextField()
    equipment = models.TextField()
    def __str__(self) -> str:
        return f"{self.teacher_allocated} teaches {self.course_tought}"
# Create your models here.

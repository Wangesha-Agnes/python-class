from classperiod.models import Class_Period
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from rest_framework import serializers
from classes.models import Classes
from teacher.models import Teacher
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
class Student_ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"
class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'
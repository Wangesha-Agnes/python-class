from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from  course.models import Course
from  classes.models import Classes
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from .serializers import StudentSerializer
from .serializers import ClassesSerializer
from .serializers import CourseSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from rest_framework.response import Response



class StudentListView(APIView):
    def get (self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self,request):
        course= Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
class  ClassesListView(APIView):
    def get (self,request):
        classes = Classes.objects.all()
        serializer =  ClassesSerializer(classes,many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)


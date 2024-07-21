# from django.shortcuts import render
# from rest_framework.views import APIView
# from student.models import Student
# from  courses.models import Courses
# from  classes.models import Classes
# from teacher.models import Teacher
# from classperiod.models import ClassPeriod
# from .serializers import StudentSerializer
# from .serializers import ClassesSerializer
# from .serializers import CoursesSerializer
# from .serializers import TeacherSerializer
# from .serializers import ClassPeriodSerializer
# from rest_framework.response import Response

# class StudentListView(APIview):
#       def get (self,request):
#           students=Student.objects.all()
#           serializer=StudentSerializer(student,mant=....)
#           return Response(serializer.data)
      
      
    #   def post(self,request);
    #        serializer = StudentSerializer(data=data=request data)
    #        if serializer.is_valid():
    #            serializer.save()
    #            return Response(serializer,status=status.HTTP_201_CREATED)
    #        else:
    #            return Response(serializer.errors, status = status.HTTP_400_BADREQUEST)


# Create your views here.

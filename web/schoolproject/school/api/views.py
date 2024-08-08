from rest_framework.views import APIView

from student.models import Student
from .serializers import StudentSerializer

from  course.models import Course
from .serializers import CourseSerializer

from  classes.models import Classes
from .serializers import ClassesSerializer


from teacher.models import Teacher
from .serializers import TeacherSerializer

from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer


from rest_framework.response import Response

from rest_framework import status


class StudentListView(APIView):
    def get(self, request):
        student = Student.objects.all()  
        country = request.query_params.get("Country")
        first_name = request.query_params.get("first_name")
        if country:
            student=Student.objects.filter(country=country)
        if first_name:
            student = student.filter(first_name=first_name)
            
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    
    def post(self,request):
           serializer = StudentSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data ,status=status.HTTP_201_CREATED)
           else:
               return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
           
class StudentDetailView(APIView):
    def enroll_student(self,student,course_id):
        course = Course.objects.get(id=course_id):
        student.courses.add(course)
    def post(self,request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action=="enrill":
            course_id=request.data.get("course_id")
            self.enroll_student(student,course_id)
        return Response(status=status.HTTP_202_ACCEPTED)    
    
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student =Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data ,status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
       
      
class CourseListView(APIView):
    def get(self,request):
        course= Course.objects.all()
        serializer = CourseSerializer(course,many=True)
        return Response(serializer.data)
    
    def post(self,request):
           serializer = CourseSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer,status=status.HTTP_201_CREATED)
           else:
               return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
           
class CourseDetailView(APIView):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self,request,id):
        course =Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data ,status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
class TeacherListView(APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    
    def post(self,request):
           serializer = TeacherSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
           else:
               return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
           
    
    
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher =Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data ,status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
       
    
class  ClassesListView(APIView):
    def get (self,request):
        classes = Classes.objects.all()
        serializer =  ClassesSerializer(classes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
           serializer = ClassesSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer,status=status.HTTP_201_CREATED)
           else:
               return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
           
           
class ClassesDetailView(APIView):
   def get(self,request,id):
        classes = Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes)
        return Response(serializer.data)
    
   def put(self,request,id):
        classes =Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data ,status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   def delete(self, request, id):
    classes = Classes.objects.get(id=id)
    classes.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

       
    
class ClassPeriodListView(APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod,many=True)
        return Response(serializer.data)
    def post(self,request):
           serializer = ClassPeriodSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer,status=status.HTTP_201_CREATED)
           else:
               return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
           
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self,request,id):
        classperiod =ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data ,status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
       


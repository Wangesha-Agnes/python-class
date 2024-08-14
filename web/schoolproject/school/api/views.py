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
           
class ClassesDetailView(APIView):
    def get_object(self, id):
        try:
            return Classes.objects.get(id=id)
        except Classes.DoesNotExist:
            raise NotFound("Class not found")

    def get(self, request, id):
        classes = self.get_object(id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)

    def put(self, request, id):
        classes = self.get_object(id)
        serializer = ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classes = self.get_object(id)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        classes = self.get_object(id)
        student_id = request.data.get("student_id")
        if student_id:
            try:
                student = Student.objects.get(id=student_id)
                classes.students.add(student)
                return Response({"detail": "Student added to class"}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Student ID is required"}, status=status.HTTP_400_BAD_REQUEST)

       
      
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
    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            raise NotFound("Course not found")

    def get(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = self.get_object(id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = self.get_object(id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        course = self.get_object(id)
        teacher_id = request.data.get("teacher_id")
        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                course.teachers.add(teacher)
                return Response({"detail": "Teacher assigned to course"}, status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                return Response({"detail": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Teacher ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    
    
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
    def get_object(self, id):
        try:
            return Classes.objects.get(id=id)
        except Classes.DoesNotExist:
            raise NotFound("Class not found")

    def get(self, request, id):
        classes = self.get_object(id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)

    def put(self, request, id):
        classes = self.get_object(id)
        serializer = ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classes = self.get_object(id)
        classes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        classes = self.get_object(id)
        teacher_id = request.data.get("teacher_id")
        if teacher_id:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                classes.teachers.add(teacher)
                return Response({"detail": "Teacher assigned to class"}, status=status.HTTP_200_OK)
            except Teacher.DoesNotExist:
                return Response({"detail": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Teacher ID is required"}, status=status.HTTP_400_BAD_REQUEST)

       
    
class ClassPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            course_id = request.data.get("course_id")
            teacher_id = request.data.get("teacher_id")
            try:
                course = Course.objects.get(id=course_id)
                teacher = Teacher.objects.get(id=teacher_id)
                serializer.save(course=course, teacher=teacher)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Course.DoesNotExist:
                return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
            except Teacher.DoesNotExist:
                return Response({"detail": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
class WeeklyTimetableView(APIView):
    def get(self, request):
        timetable_data = self.get_weekly_timetable()
        return Response(timetable_data)

    def get_weekly_timetable(self):
        periods = ClassPeriod.objects.all()
        timetable = []
        for period in periods:
            timetable.append({
                "day": period.day,
                "start_time": period.start_time,
                "end_time": period.end_time,
                "course": period.course.name,
                "teacher": period.teacher.name,
                "class": period.class.name
            })
        return timetable

 
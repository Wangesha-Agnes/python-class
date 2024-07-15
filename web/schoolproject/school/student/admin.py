from django.contrib import admin

from .models import Student

admin.site.register(Student)

# Register your models here.

# class StudentListView(Apiview):
#       def get(self,requwst):
#           Students=Student.objects.all()
#           serializer=StudentSerializer(Students,many=true)
#           return Response(serializer.data)


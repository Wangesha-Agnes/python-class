from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import ClassesListView
from .views import CourseListView
from .views import ClassPeriodListView

urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    # path("students/",StudentListView.as_views),name="student_list_view"
    path("teachers/", TeacherListView.as_view(),name="teacher_list_view"),
    path("classes/", ClassesListView.as_view(),name="class_list_view"),
    path("course/", CourseListView.as_view(),name="course_list_view"),
    path("classperiod/", ClassPeriodListView.as_view(),name="classperiod_list_view")

]
   
# Create your views here.


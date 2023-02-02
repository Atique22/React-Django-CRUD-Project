from django.urls import path
from api import views
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('teacher/', views.TeacherList.as_view()),
     path('add/', views.add, name='add'),
]

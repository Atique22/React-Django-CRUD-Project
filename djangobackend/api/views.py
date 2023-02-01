from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Students
# Create your views here.
class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
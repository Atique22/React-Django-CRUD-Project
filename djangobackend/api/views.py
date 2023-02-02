from django.shortcuts import render
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from rest_framework.generics import ListAPIView
# from django.views import View
from django.http import JsonResponse
from .models import Students
from .models import Teachers
# Create your views here.
class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
            name = request.POST.get('name')
            email = request.POST.get('email')
            # process the data, such as saving it to the database
            user = Students.objects.create(studName=name, studEmail=email)
            return JsonResponse({'message': 'Data created successfully'})

class TeacherList(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

from django.shortcuts import render
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from rest_framework.generics import ListAPIView
# from django.views import View
import json
from django.http import JsonResponse
from .models import Students
from .models import Teachers
# Create your views here.
class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        if request.method == 'POST':
            body = json.loads(request.body.decode('utf-8'))
            print(body.get('studName'))
            print(body.get('studEmail'))
            stud_name =  body.get('studName')
            stud_email = body.get('studEmail')
            print(stud_name)
            print(stud_email)
            # stud_name = "Atique"
            # stud_email = "Atique@gamil.com"
            if stud_name and stud_email:
                 student = Students(studName=stud_name, studEmail=stud_email)
                 student.save()

            return JsonResponse({'message': 'Student created successfully'})
        return JsonResponse({'error': 'Invalid request method'})



class TeacherList(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request):
        if request.method == 'POST':
            tecName = request.POST.get('tecName')
            techEmail = request.POST.get('techEmail')
            techPhone = request.POST.get('techPhone')

            teacher = Teachers(tecName=tecName, techEmail=techEmail, techPhone=techPhone)
            teacher.save()

            return JsonResponse({'message': 'Student created successfully'})
        return JsonResponse({'error': 'Invalid request method'})

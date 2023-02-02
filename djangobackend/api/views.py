from django.shortcuts import render
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from .models import Students
from .models import Teachers
# Create your views here.
class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class TeacherList(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

def add(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        # process the received data
        # ...

        return JsonResponse({'message': 'Data received successfully'})

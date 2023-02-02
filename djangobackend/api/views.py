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

    # def post(self, request, *args, **kwargs):
    # #    StudentSerializer(data=request.)
    #         name = request.POST.get('studName')
    #         email = request.POST.get('studEmail')
    #         # process the data, such as saving it to the database
    #         user = Students.objects.create(studName=name, studEmail=email)
    #         return JsonResponse({'message': 'Data created successfully'})

    def post(self, request):
        if request.method == 'POST':
            stud_name = request.POST.get('studName')
            stud_email = request.POST.get('studEmail')

            student = Students(studName=stud_name, studEmail=stud_email)
            student.save()

            return JsonResponse({'message': 'Student created successfully'})
        return JsonResponse({'error': 'Invalid request method'})

class TeacherList(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

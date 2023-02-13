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

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            stud_name = request.POST.get('studName')
            stud_email = request.POST.get('studEmail')

            if stud_name:
                student = Students(studName=stud_name, studEmail=stud_email)
                student.save()

            return JsonResponse({'message': 'data created successfully'})
        return JsonResponse({'error': 'Invalid request method'})


def delete_records(request, idDelete):
    # if request.method == "DELETE":
    item_id = int(idDelete)
    try:
        item = Students.objects.get(id=item_id)
    except Students.DoesNotExist:
        return JsonResponse({'message': 'Item deleted errors'})
    item.delete()
    # return redirect('http://localhost:3000/BackendViewData')
    return JsonResponse({'message': 'Item deleted successfully'})


class TeacherList(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request):
        if request.method == 'POST':
            tecName = request.POST.get('tecName')
            techEmail = request.POST.get('techEmail')
            techPhone = request.POST.get('techPhone')

            teacher = Teachers(
                tecName=tecName, techEmail=techEmail, techPhone=techPhone)
            teacher.save()

            return JsonResponse({'message': 'Student created successfully'})
        return JsonResponse({'error': 'Invalid request method'})

    # def post(self, request):
    #     if request.method == 'POST':
    #         body = json.loads(request.body.decode('utf-8'))
    #         print(body.get('studName'))
    #         print(body.get('studEmail'))
    #         stud_name =  body.get('studName')
    #         stud_email = body.get('studEmail')
    #         print(stud_name)
    #         print(stud_email)
    #         # stud_name = "Atique"
    #         # stud_email = "Atique@gamil.com"
    #         if stud_name and stud_email:
    #              student = Students(studName=stud_name, studEmail=stud_email)
    #              student.save()

    #         return JsonResponse({'message': 'Student created successfully'})
    #     return JsonResponse({'error': 'Invalid request method'})

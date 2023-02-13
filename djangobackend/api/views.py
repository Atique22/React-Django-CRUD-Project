from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from django.views import View
import json
from django.http import JsonResponse
from .models import Students
# Create your views here.


class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            stud_name = request.POST.get('studentName')
            stud_email = request.POST.get('studentEmail')

            if stud_name:
                student = Students(studentName=stud_name,
                                   studentEmail=stud_email)
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
    return JsonResponse({'message': 'Item deleted successfully'})


def update_records(request, idUpdate, *args, **kwargs):
    # if request.method == "DELETE":
    item_id = int(idUpdate)
    print(item_id)
    try:
        instance = Students.objects.get(id=item_id)
        if request.method == 'POST':
            # Update the model instance with the new data
            instance.studentName = request.POST.get('studentName')
            instance.studentEmail = request.POST.get('studentEmail')
            instance.save()
    except Students.DoesNotExist:
        return JsonResponse({'message': 'Item update errors'})
    return JsonResponse({'message': 'Item update successfully'})

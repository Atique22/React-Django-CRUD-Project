from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from django.views import View
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
    if request.method == "put":
        item_id = int(idUpdate)
        instance = get_object_or_404(Students, id=item_id)
        data = request.body
        # convert the json data to python dictionary
        data = json.loads(data)
        # update the fields with the new values
        instance.studentName = data.get('studentName', instance.studentName)
        instance.studentEmail = data.get('studentEmail', instance.studentEmail)
        instance.save()
        return JsonResponse({"message": "Item updated successfully"})
    return JsonResponse({"message": "Invalid request method"})

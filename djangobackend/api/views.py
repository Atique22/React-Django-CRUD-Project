from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Students
# Create your views here.


class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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

    def put(self, request, *args, **kwargs):
        item_id = kwargs.get('idUpdate')
        item = get_object_or_404(Students, id=item_id)

        stud_name = request.POST.get('studentName')
        stud_email = request.POST.get('studentEmail')

        if stud_name:
            item.studentName = stud_name
            item.studentEmail = stud_email
            item.save()
            return JsonResponse({'message': 'Data updated successfully'})
        else:
            return JsonResponse({'error': 'Please provide a student name'})

    def delete(self, request, *args, **kwargs):
        item_id = kwargs.get('idDelete')
        item = get_object_or_404(Students, id=item_id)
        item.delete()
        return JsonResponse({'message': 'Data deleted successfully'})


# def delete_records(request, idDelete):
#     print(request.method)
#     if request.method == "DELETE":
#         item_id = int(idDelete)
#         try:
#             item = Students.objects.get(id=item_id)
#         except Students.DoesNotExist:
#             return JsonResponse({'message': 'Item deleted errors'})
#         item.delete()
#         return JsonResponse({'message': 'Item deleted successfully'})

        # stud_name = request.PUT.get('studentName')
        # stud_email = request.PUT.get('studentEmail')

        # if stud_name:
        #     student = Students(studentName=stud_name,
        #                        studentEmail=stud_email)
        #     student.save()

        # print("helo ")
        # item_id = int(idUpdate)
        # instance = get_object_or_404(Students, id=item_id)
        # instance = Students.objects.get(id=item_id)
        # data = json.loads(request.body.decode())

        # data = request.GET.get('studentName')
        # print(data)
        # print(instance.studentName)
        # print("post name:"+request.POST.get(
        #     'studentName'))
        # print("backend name:"+instance.studentName)
        # # convert the json data to python dictionary
        # data = json.loads(data)
        # # update the fields with the new values
        # instance.studentName = "ali irfan"
        # instance.studentName = request.PUT.get(
        #     'studentName')
        # instance.studentEmail = request.PUT.get(
        #     'studentEmail')
        # instance.save()
    #     return JsonResponse({"message": "Item updated successfully"})
    # return JsonResponse({"message": "Invalid request method"})

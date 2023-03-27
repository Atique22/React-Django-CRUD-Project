
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .serializers import StudentSerializer
from .serializers import FrameSerializer
from rest_framework.generics import ListAPIView
# from django.views import View
import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Students
from .models import Frame
import base64
from io import BytesIO
from PIL import Image
# Create your views here.


class FrameList(ListAPIView):
    queryset = Frame.objects.all()
    serializer_class = FrameSerializer

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("yes post is working ")
            frameName = request.POST.get('frameName')
            frameType = request.POST.get('frameType')
            frameComment = request.POST.get('frameComment')
            frameImage = request.POST.get('frameImage')
            print("name", frameName)
            print("type", frameType)
            print("comment", frameComment)
            # print("image", frameImage)
            if frameName:
                # decode the base64 image data into bytes
                # remove the "data:image/jpeg;base64," prefix
                data = frameImage.split(',')[1]
                image_bytes = base64.b64decode(data)
                image = Image.open(BytesIO(image_bytes))
                # generate a new filename based on the current timestamp
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f'captured_frame_{timestamp}.jpg'

                # save the image to a file with the new filename
                image.save(filename)

                # create a new Frame object and save it to the database
                frame_data = Frame(frame_name=frameName, frame_type=frameType,
                                   frame_comment=frameComment, frame_image=filename)
                frame_data.save()

            return JsonResponse({'message': 'frame data created successfully'})
        return JsonResponse({'error': 'Invalid request method'})


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
        print("hello there")
        if request.method == "PUT":
            print("PUT IS WORKING ")
            item_id = kwargs.get('idUpdate')
            print(item_id)
            item = get_object_or_404(Students, id=item_id)
            print(item.studentName)
            stud_name = request.data.get('studentName')
            stud_email = request.data.get('studentEmail')
            print(stud_name)
            print(stud_email)
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

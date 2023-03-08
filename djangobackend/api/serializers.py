from rest_framework import serializers
from .models import Students
from .models import Frame


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'studentName', 'studentEmail']


class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ['frame_name', 'frame_type', 'frame_comment', 'frame_image']

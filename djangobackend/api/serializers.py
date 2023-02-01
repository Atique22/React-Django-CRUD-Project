from rest_framework import serializers
from .models import Students
from .models import Teachers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'studName','studEmail']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'tecName','techEmail','techPhone']
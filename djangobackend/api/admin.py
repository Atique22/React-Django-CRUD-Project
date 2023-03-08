from django.contrib import admin
from .models import Students
from .models import Frame
# Register your models here.


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'studentName', 'studentEmail']


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ['id', 'frame_name', 'frame_type',
                    'frame_comment', 'frame_image']

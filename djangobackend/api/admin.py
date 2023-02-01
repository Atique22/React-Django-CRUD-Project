from django.contrib import admin
from .models import Students
from .models import Teachers
# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'studName','studEmail']
    
@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'tecName','techEmail','techPhone']
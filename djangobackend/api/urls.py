from django.urls import path
from api import views
# from django.conf import settings
# from .views import delete_records
# from .views import update_records


urlpatterns = [
    path('student/', views.StudentList.as_view(),
         name='student read and create-data'),
    path('teacher/', views.TeacherList.as_view(),
         name='teacher read and create-data'),
    path('delete/<int:idDelete>/', views.delete_records, name='idDelete'),
    path('update/<int:idUpdate>/', views.update_records, name='update records'),
]

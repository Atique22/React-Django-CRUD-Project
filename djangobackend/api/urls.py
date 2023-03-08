from django.urls import path
from .views import StudentList
from .views import FrameList

urlpatterns = [
    path('api/frameDataStorage', FrameList.as_view(), name='frame sets'),
    path('api/students', StudentList.as_view(), name='students'),
    path('api/delete/<int:idDelete>', StudentList.as_view(), name='delete'),
    path('api/update/<int:idUpdate>', StudentList.as_view(), name='update'),
]


# from django.urls import path
# from api import views
# from . import views

# urlpatterns = [
#     path('student/', views.StudentList.as_view(),
#          name='student read and create-data'),
#     path('delete/<int:idDelete>', views.delete_records, name='Delete records'),
#     path('update/<int:idUpdate>',
#          views.update_records, name='update records'),
# ]

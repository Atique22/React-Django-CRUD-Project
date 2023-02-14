from django.urls import path
from api import views
from . import views

urlpatterns = [
    path('student/', views.StudentList.as_view(),
         name='student read and create-data'),
    path('delete/<int:idDelete>', views.delete_records, name='Delete records'),
    path('update/<int:idUpdate>',
         views.update_records, name='update records'),
]

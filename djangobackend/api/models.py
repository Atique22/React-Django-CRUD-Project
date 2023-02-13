from django.db import models
# Create your models here.


class Students(models.Model):
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField(max_length=100)

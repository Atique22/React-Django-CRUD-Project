from django.db import models

# Create your models here.

class Students(models.Model):
    studName = models.CharField(max_length=100);
    studEmail = models.EmailField(max_length=100);
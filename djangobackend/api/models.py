from django.db import models
# Create your models here.

class Students(models.Model):
    studName = models.CharField(max_length=100);
    studEmail = models.EmailField(max_length=100);
class Teachers(models.Model):
    tecName = models.CharField(max_length=100);
    techEmail = models.CharField(max_length=100);
    techPhone = models.CharField(max_length=12);
from django.db import models
# Create your models here.


class Students(models.Model):
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField(max_length=100)


class Frame(models.Model):
    frame_name = models.CharField(max_length=100)
    frame_type = models.CharField(max_length=50)
    frame_comment = models.TextField()
    frame_image = models.ImageField(upload_to='frame_images/')
    created_at = models.DateTimeField(auto_now_add=True)

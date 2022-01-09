from django.db import models
from django.conf import settings
# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=500)
    date=models.DateField()
    time= models.TimeField()
    location=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images/')
    is_liked=models.BooleanField(default=False)
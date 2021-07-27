from django.db import models
from datetime import date


class Students(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentFirstName = models.CharField(max_length=100)
    studentLastName = models.CharField(max_length=100)
    studentLevel = models.CharField(max_length=100)
    studentEcode = models.CharField(max_length=100, default="EH174012")
    studentAge = models.IntegerField()
    dateOfJoining = models.DateField(default=date.today)
    studentPhotoName = models.CharField(max_length=100)



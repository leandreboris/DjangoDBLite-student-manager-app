from rest_framework import serializers
from StudentsApp.models import Students



class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('studentId', 'studentFirstName', 'studentLastName', 'studentLevel', 'studentEcode', 'studentAge', 'dateOfJoining', 'studentPhotoName')
        
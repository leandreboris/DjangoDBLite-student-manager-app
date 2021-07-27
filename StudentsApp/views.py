from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import  JSONParser
from django.http.response import JsonResponse

from StudentsApp.models import Students
from StudentsApp.serializer import  StudentsSerializer


from django.core.files.storage import default_storage


@csrf_exempt
def studentApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            student = Students.objects.get(studentId=id)
            students_serializer = StudentsSerializer(student)
            return JsonResponse(students_serializer.data, safe = False)
        students = Students.objects.all()
        students_serializer = StudentsSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe = False)
    
    elif request.method=='POST':
        students_data=JSONParser().parse(request)
        students_serializer = StudentsSerializer(data=students_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    elif request.method=='PUT':
        students_data = JSONParser().parse(request)
        students = Students.objects.get(studentId=students_data['studentId'])
        students_serializer = StudentsSerializer(students, data=students_data)
        if students_serializer.is_valid() :
            students_serializer.save()
            return JsonResponse("Updated succesfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE' :
        students = Students.objects.get(studentId=id)
        students.delete()
        return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def savePicture(request):
    file = request.FILES['uploadedPicture']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from databaseModels.models import StudentapiStudentinfo
from databaseModels.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def studentInfo(request,id=None):
    if request.method == 'GET' and id: 
        studentById= StudentapiStudentinfo.objects.filter( studentrollno = id ) 
        student_serialize = StudentSerializer(studentById,many=True)
        return JsonResponse(student_serialize.data,safe = False)
    
    elif request.method == 'GET':
        students = StudentapiStudentinfo.objects.all().order_by('studentrollno')
        student_serialize = StudentSerializer(students,many=True)
        return JsonResponse(student_serialize.data,safe=False)

    if request.method == 'DELETE':
        student = StudentapiStudentinfo.objects.get(studentrollno=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
    if request.method == 'POST':
        studentrequestBody = JSONParser().parse(request)
        serializeBody = StudentSerializer(data=studentrequestBody)
        if studentrequestBody.is_valid():
            studentrequestBody.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed Check data",safe = False)

    if request.method == 'PUT':
        studentrequestBody = JSONParser().parse(request)
        studentId = StudentapiStudentinfo.objects.get(studentrollno=studentrequestBody['studentrollno'])
        serializeStudentBody = StudentSerializer(studentId,data=studentrequestBody)
        if serializeStudentBody.is_valid():
            serializeStudentBody.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed Check data",safe = False)


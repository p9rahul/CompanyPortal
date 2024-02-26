from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .serializers import EmployeeDetailsserializer
from .models import EmployeeDetails

@csrf_exempt
def employee(request, id=0):
    if request.method=='GET':
       emp_all = EmployeeDetails.objects.all()
       if(id==0):
           emp_serializer=EmployeeDetailsserializer(emp_all,many=True)
       else:
          emp_byID= emp_all.filter(emp_id=id)
          emp_serializer=emp_serializer(emp_byID,many=True)
       return JsonResponse(emp_serializer.data,safe=False)
    elif request.method=='POST':
       emp_data = JSONParser().parse(request)
       emp_serializer = EmployeeDetailsserializer(data=emp_data)
       if emp_serializer.is_valid():
          emp_serializer.save()
          return JsonResponse(emp_serializer.data,safe=False)
       return JsonResponse("Failed POST",safe=False)
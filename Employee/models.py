from django.db import models
from django.utils import timezone

# Create your models here.
class EmployeeDetails(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_Name=models.CharField(max_length=100)
    emp_Dept=models.CharField(max_length=100)
    emp_location=models.CharField(max_length=100)
    emp_country=models.CharField(max_length=100)

# class ParamsAPI(models.Model):
#     param_key = models.CharField(max_length=100)
#     param_value = models.CharField(max_length=100)
#     request = models.ForeignKey(EmployeeDetails, related_name='requests',on_delete=models.CASCADE,default=1)
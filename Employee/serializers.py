from rest_framework import serializers
from .models import EmployeeDetails

# class Paramserializer(serializers.ModelSerializer):
#     class Meta:
#         model = ParamsAPI
#         fields = "__all__"

class EmployeeDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model =EmployeeDetails
        fields = "__all__"


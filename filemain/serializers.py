from rest_framework import serializers
from . models import Employee

class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
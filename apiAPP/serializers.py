from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator


class apiapp_serializers(serializers.ModelSerializer):
    code = serializers.CharField(
        read_only=True
    )
    client_contactnumber = serializers.IntegerField(
        validators=[UniqueValidator(queryset=Fields.objects.all())]
    )
    revenue = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model=Fields
        fields = ['code','customer_name','email','survey','status','Emp_type','start_date','end_date','revenue','cpi','completes','client_contactnumber']
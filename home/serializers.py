from rest_framework.serializers import Serializer
from rest_framework import serializers
from  .models import *


class StudentSerializer  (serializers.ModelSerializer):
    class Meta:
        model= Student
        exclude= ['id']
        # fields = '__all__'
        # fields = ['name', 'age']
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({'error':'age cna not be less than 18'})
        for char in data['name']:
            if char.isdigit():
                raise serializers.ValidationError({'error':'name can not contain any number.'})
        return data
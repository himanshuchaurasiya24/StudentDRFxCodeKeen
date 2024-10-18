from rest_framework.serializers import Serializer
from rest_framework import serializers
from  .models import *
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username', 'password']
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        # to encrypt the password user setpassword method like below
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model= Student
        # exclude= ['id']
        fields = '__all__'
        # fields = ['name', 'age']
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({'error':'age can not be less than 18'})
        for char in data['name']:
            if char.isdigit():
                raise serializers.ValidationError({'error':'name can not contain any number.'})
        return data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields='__all__'
        # fields=['category_name']
class BookSerializer (serializers.ModelSerializer):
    # pass CategorySerializer() as category is given as a foreign key.
    category = CategorySerializer()    
    class Meta:
        model = Book
        fields= '__all__'
        # either pass depth or the category in this case for inclusion of foreign key model data depth will contain
        # all the data of the foreign key and pass it to the api whereas category will allow to pass the data defined in the category serializer 'fields' attributes
        # depth=1
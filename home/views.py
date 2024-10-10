from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from home.models import *

@api_view(['GET'])
def home(request):
    studet_obj = Student.objects.all()
    serializer = StudentSerializer(studet_obj, many = True)
    return Response({'status':200, 
                     'message':'Django REST Framework', 
                     'data':serializer.data,})
@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data= data)
    if not serializer.is_valid():
        return Response({'status':400,
                         'message':'data is in incorrect format', 
                         'error':serializer.errors}) 
    serializer.save()
    return Response({'status':200, 
                     'message':'student added successfully', 
                     'data':serializer.data,})


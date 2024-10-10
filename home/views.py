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
@api_view(['PUT'])
def update_student(request):
    try:
        student_obj= Student.objects.get(id = request.data['id'])
        serializer = StudentSerializer(student_obj, data= request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'message':'Invalid data format', 'error':serializer.errors})
        serializer.save()
        return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})

    except Exception as e:
        return Response({'status':403, 'message':'Error while updating the data', 'error':e})

@api_view(['PATCH'])
def partial_update_student(request):
    try:
        data = request.data
        student_obj = Student.objects.filter(id = data.get('id'))
        print(student_obj[0])
        print(student_obj)
        print(request.data.get('id'))
        if not student_obj.exists():
            return Response({'status':404, 'message':'no student found of this id', 'id':request.data.get('id')})
        serializer= StudentSerializer(student_obj[0], data=data, partial=True)
        if not serializer.is_valid():
            return Response({'status':403, 'message':'Invalid data format', 'error':serializer.errors})
        serializer.save()
        return Response({'status':201, 'message':'partial data updated successfully', 'data':serializer.data})
    except Exception as e:
        return Response({'status':400, 'message':'some exception came while partially updating the data', 'error':e})
@api_view(['DELETE'])
def delete_student(request):
    try:
        data= request.data
        student_obj = Student.objects.filter(id = data['id'])
        if not student_obj.exists():
            return Response({'status':404, 'message':'No student found of this id'} )
        else:
            student_obj[0].delete()
            print('student deleted successfully')
            return Response({'status':200, 'message':'student deleted successfully'})
    except Exception as e:
        return Response({'status':400 , 'message':'some exception came while trying to delete this student'})
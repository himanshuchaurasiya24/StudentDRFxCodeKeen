from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from home.models import *

@api_view(['GET'])
def get_category(request):
    try:
        category_obj = Category.objects.all()
        serializer = CategorySerializer(category_obj, many = True)
        return Response({'status':200,'data':serializer.data})
    except Exception as e:
        return Response({'status':400,'error':e})
@api_view(['POST'])
def post_category(request):
    try:
        data = request.data
        serializer = CategorySerializer(data= data, )
        if not serializer.is_valid():
            return Response({'status':400, 'message':'category data is in incorrect format', 'data':data})
        serializer.save()
        return Response({'status':202, 'message':'category added successfully', 'data':data})
    except Exception as e:
        return Response({'status':400, 'message':'some exception while adding the category', 'error':e})
@api_view(['PUT'])
def update_category(request):
    try:
        category_obj= Category.objects.filter(id = request.data['id'])
        if len(category_obj)==0:
            return Response({'status':403, 'message':'No category found', 'data':request.data})
        else:
            serializer = CategorySerializer(category_obj[0], data= request.data)
            if not serializer.is_valid():
                return Response({'status':403, 'message':'Invalid data format', 'error':serializer.errors})
            serializer.save()
            return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})
    except Exception as e:
        return Response({'status':403, 'message':'Error while updating the data', 'error':e})
@api_view(['PATCH'])
def patch_category(request):
    try:
        category_obj= Category.objects.filter(id = request.data['id'])
        print(len(category_obj))
        if len(category_obj)==0:
            return Response({'status':403, 'message':'No category found', 'data':request.data})
        else:
            if 'category_name' in request.data:
                category_obj[0].book_title=request.data['category_name']
            category_obj[0].save()
            return Response({'status':200, 'message':'partial updation was successful', 'data':request.data})
    except Exception as e:
        return Response({'status':400, 'message':'some exception while updating the category partially', 'exception':e})
@api_view(['DELETE'])
def delete_category(request):
    data = request.data
    category_obj = Category.objects.filter(id = data['id'])
    category_obj[0].delete()
    return Response({'status':200, 'message':'category deleted'})

























@api_view(['GET'])
def get_book(request):
    try:
        book_obj = Book.objects.all()
        serializer = Bookserializer(book_obj, many = True)
        return Response({'status':200,'data':serializer.data})
    except Exception as e:
        return Response({'status':400,'error':e})
@api_view(['POST'])
def post_book(request):
    try:
        data = request.data
        serializer = Bookserializer(data= data, )
        if not serializer.is_valid():
            return Response({'status':400, 'message':'book data is in incorrect format', 'data':data})
        serializer.save()
        return Response({'status':202, 'message':'book added successfully', 'data':data})
    except Exception as e:
        return Response({'status':400, 'message':'some exception while adding the book', 'error':e})
@api_view(['PUT'])
def update_book(request):
    try:
        book_obj= Book.objects.filter(id = request.data['id'])
        if len(book_obj)==0:
            return Response({'status':403, 'message':'No book found', 'data':request.data})
        else:
            serializer = Bookserializer(book_obj[0], data= request.data)
            if not serializer.is_valid():
                return Response({'status':403, 'message':'Invalid data format', 'error':serializer.errors})
            serializer.save()
            return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})
    except Exception as e:
        return Response({'status':403, 'message':'Error while updating the data', 'error':e})
@api_view(['PATCH'])
def patch_book(request):
    try:
        data = request.data
        book_obj = Book.objects.get(id = data['id'])  
        if book_obj.DoesNotExist:
            return Response({'status':404, 'message':'No book found of this id', 'data':data})      
        if 'book_title' in data:
            book_obj.book_title=data['book_title']
        if 'category' in data:
            book_obj.category=data['category']
        book_obj.save()
        return Response({'status':200, 'message':'partial updation was successful', 'data':data})
    except Exception as e:
        return Response({'status':400, 'message':'some exception while updating the book partially', 'exception':e})
@api_view(['DELETE'])
def delete_book(request):
    data = request.data
    book_obj = Book.objects.get(id = data['id'])
    if book_obj.DoesNotExist:
            return Response({'status':404, 'message':'No book found of this id', 'data':data})
    book_obj.delete()
    return Response({'status':200, 'message':'book deleted'})

            

















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
        student_obj= Student.objects.filter(id = request.data['id'])
        if len(student_obj)==0:
            return Response({'status':403, 'message':'No student found', 'data':request.data})
        else:
            serializer = StudentSerializer(student_obj[0], data= request.data)
            if not serializer.is_valid():
                return Response({'status':403, 'message':'Invalid data format', 'error':serializer.errors})
            serializer.save()
            return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})
    except Exception as e:
        return Response({'status':403, 'message':'Error while updating the data', 'error':e})

@api_view(['PATCH'])
def partial_update_student(request):
    data = request.data
    try:
        student = Student.objects.get(id=data['id'])
    except Student.DoesNotExist:
        return Response({'error':'does not exists'})
    if 'name' in data:
        student.name = data['name']
    if 'age' in data:
        student.age = data['age']
    if 'father_name' in data:
        student.father_name = data['father_name']
    student.save()
    return Response({"message": "Student updated successfully"})
    # try:
    #     data = request.data
    #     student_obj = Student.objects.filter(id = data.get('id'))
    #     print(student_obj[0])
    #     print(student_obj)
    #     print(request.data.get('id'))
    #     if not student_obj.exists():
    #         return Response({'status':404, 'message':'no student found of this id', 'id':request.data.get('id')})
    #     serializer= StudentSerializer(student_obj[0], data=data, partial=True)
    #     if not serializer.is_valid():
    #         return Response({'status':403, 'message':'Invalid data format', 'error':serializer.errors})
    #     serializer.save()
    #     return Response({'status':201, 'message':'partial data updated successfully', 'data':serializer.data})
    # except Exception as e:
    #     return Response({'status':400, 'message':'some exception came while partially updating the data', 'error':e})
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
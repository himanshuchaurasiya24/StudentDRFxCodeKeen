from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from home.models import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
class RegisterUserAPIView(APIView):
    
    def post(self, request):
        data = request.data
        serializer= UserSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':404,'message':'some error while logging in. Check credentials and its format', 'data':serializer.errors})
        serializer.save()
        user =User.objects.get(username=data['username'])
        # in serializers of user in create method setpassword method is used to encrypt the password
        # session authentication method is used here...
        token_obj , _=Token.objects.get_or_create(user=user)
        return Response({'status':202, 'message':serializer.data, 'data':str(token_obj)})
class StudentAPIView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        stu_objs = Student.objects.all()
        serializer = StudentSerializer(stu_objs, many=True)
        return Response({'status':200, 'message':'student list fetched.', 'data':serializer.data})
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data= data)
        if not serializer.is_valid():
            return Response({'status':400,
                             'message':'data is in incorrect format', 
                             'data':serializer.errors}) 
        serializer.save()
        return Response({'status':200, 
                         'message':'student added successfully', 
                         'data':serializer.data,})
    def put(self, request):
        try:
            student_obj= Student.objects.filter(id = request.data['id'])
            if len(student_obj)==0:
                return Response({'status':403, 'message':'No student found', 'data':request.data})
            else:
                serializer = StudentSerializer(student_obj[0], data= request.data)
                if not serializer.is_valid():
                    return Response({'status':403, 'message':'Invalid data format', 'data':serializer.errors})
                serializer.save()
                return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})
        except Exception as e:
            return Response({'status':403, 'message':e, 'data':request.data})
    def patch(self, request):
        data = request.data
        try:
            student = Student.objects.get(id=data['id'])
            if 'name' in data:
                student.name = data['name']
            if 'age' in data:
                student.age = data['age']
            if 'father_name' in data:
                student.father_name = data['father_name']
            student.save()
            return Response({'status':202,'data':request.data,
                "message": "Student updated successfully"})
        except Student.DoesNotExist:
            return Response({"status":404, 
                             'message':'no student found for this id',
                'data':'does not exists'})
       
    def delete(self, request):
        try:
            data= request.data
            student_obj = Student.objects.filter(id = data['id'])
            if not student_obj.exists():
                return Response({'status':404, 'message':'No student found of this id', 'data':''} )
            else:
                student_obj[0].delete()
                return Response({'status':200, 'message':'student deleted successfully', 'data':''})
        except Exception as e:
            return Response({'status':400 , 'message':'some exception came while trying to delete this student', 'data':e})
class CategoryAPIView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            category_obj = Category.objects.all()
            serializer = CategorySerializer(category_obj, many = True)
            return Response({'status':200,'data':serializer.data,'message':'category fetched successfully'})
        except Exception as e:
            return Response({'status':400,'data':e, 'message':'some error while fetching the category from the database'})

    def post(self, request):
        try:
            data = request.data
            serializer = CategorySerializer(data= data, )
            if not serializer.is_valid():
                return Response({'status':400, 'message':'category data is in incorrect format', 'data':data})
            serializer.save()
            return Response({'status':202, 'message':'category added successfully', 'data':data})
        except Exception as e:
            return Response({'status':400, 'message':'some exception while adding the category', 'data':e})
    def put(self, request):
        try:
            category_obj= Category.objects.filter(id = request.data['id'])
            if len(category_obj)==0:
                return Response({'status':403, 'message':'No category found', 'data':request.data})
            else:
                serializer = CategorySerializer(category_obj[0], data= request.data)
                if not serializer.is_valid():
                    return Response({'status':403, 'message':'Invalid data format', 'data':serializer.errors})
                serializer.save()
                return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})
        except Exception as e:
            return Response({'status':403, 'message':'Error while updating the data', 'data':e})
    def patch(self, request):
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
    def delete(self, request):
        data = request.data
        category_obj = Category.objects.filter(id = data['id'])
        category_obj[0].delete()
        return Response({'status':200, 'message':'category deleted'})
class BookAPIView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            book_obj = Book.objects.all()
            serializer = BookSerializer(book_obj, many = True)
            return Response({'status':200,'data':serializer.data,'message':'book fetched successfully'})
        except Exception as e:
            return Response({'status':400,'data':e, 'message':'some error while fetching the book from the database'})

    def post(self, request):
        try:
            data = request.data
            serializer = BookSerializer(data= data, )
            if not serializer.is_valid():
                return Response({'status':400, 'message':'book data is in incorrect format', 'data':data})
            serializer.save()
            return Response({'status':202, 'message':'book added successfully', 'data':data})
        except Exception as e:
            return Response({'status':400, 'message':'some exception while adding the book', 'data':e})
    def put(self, request):
        try:
            book_obj= Book.objects.filter(id = request.data['id'])
            if len(book_obj)==0:
                return Response({'status':403, 'message':'No book found', 'data':request.data})
            else:
                serializer = BookSerializer(book_obj[0], data= request.data)
                if not serializer.is_valid():
                    return Response({'status':403, 'message':'Invalid data format', 'data':serializer.errors})
                serializer.save()
                return Response({'status':200, 'message':'data updated successfuly', 'data':serializer.data})
        except Exception as e:
            return Response({'status':403, 'message':'Error while updating the data', 'data':e})
    def patch(self, request):
        try:
            book_obj= Book.objects.filter(id = request.data['id'])
            print(len(book_obj))
            if len(book_obj)==0:
                return Response({'status':403, 'message':'No book found', 'data':request.data})
            else:
                if 'book_title' in request.data:
                    book_obj[0].book_title=request.data['book_title']
                if 'category' in request.data:
                    book_obj[0].category=request.data['category']
                book_obj[0].save()
                return Response({'status':200, 'message':'partial updation was successful', 'data':request.data})
        except Exception as e:
            return Response({'status':400, 'message':'some exception while updating the book partially', 'exception':e})
    def delete(self, request):
        data = request.data
        book_obj = Book.objects.filter(id = data['id'])
        book_obj[0].delete()
        return Response({'status':200, 'message':'book deleted'})

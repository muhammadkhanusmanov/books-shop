from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpRequest,JsonResponse,FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication



from .serializers.author_serializers import AuthorSerializer
from .serializers.genre_serializers import GenreSerializer
from .serializers.publisher_serializers import PublisherSerializer
from .serializers.language_serializers import LanguageSerializer
from .serializers.book_serializers import BookSerializer
from .serializers.bookimage_serializers import BookImageSerializer

from .models import BookImage,Book,Genre,Author,Language,Publisher

class GenreView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request):
        data = request.data
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class AuthorView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class PublisherView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self,request):
        data = request.data
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

class LanguageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self,request:Request):
        data = request.data
        serializer = LanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

class BookView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

class BookImageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        data = request.data
        serializer = BookImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status':'Created'},status=status.HTTP_201_CREATED)
        return Response({'Status':'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username',None)
        password = data.get('password',None)
        first_name = data.get('first_name',username)
        if username is not None and first_name is not None:
            try:
                user = User.objects.get(username=username)
                return Response({'Status':'This username is already'},status=status.HTTP_208_ALREADY_REPORTED)
            except:
                user = User.objects.create(
                    username=username,
                    password=make_password(password),
                    first_name=first_name
                )
                user.save()
                token = Token.objects.create(user=user)
                return Response({'Status':'created','Token':token.key},status=status.HTTP_201_CREATED)
        return Response({'Status':'BAD_REQUEST'},status=status.HTTP_400_BAD_REQUEST)
    authentication_classes = [BasicAuthentication]
    def put(self,request):
        user = request.user
        print(user)
        try:
            token,created = Token.objects.get_or_create(user = user)
            return Response({'Status': 'OK','Token': token.key},status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'User not found', 'Token':None},status=status.HTTP_404_NOT_FOUND)

class LogOut(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        user = request.user
        try:
            token = Token.objects.get(user=user)
            token.delete()
            return Response({'Status': 'Deleted token'},status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'Bad request'},status=status.HTTP_400_BAD_REQUEST)



class GetGenreView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genres = GenreSerializer(genres,many=True)
        return Response(genres.data)
    def put(self, request, id: int):
        try:
            genre = Genre.objects.get(id=id)
            serializer = GenreSerializer(data=genre)
            return Response(serializer.data)
        except:
            return Response({'Status':'Genre not found'}, status=status.HTTP_404_NOT_FOUND)

class GetAuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        authors = AuthorSerializer(authors,many=True)
        return Response(authors.data)
    def put(self, request, id: int):
        try:
            author = Author.objects.get(id=id)
            serializer = AuthorSerializer(data=author)
            return (serializer.data)
        except:
            return Response({'Status':'Author not found'}, status=status.HTTP_404_NOT_FOUND)

class GetLanguageView(APIView):
    def get(self, request):
        languages = Language.objects.all()
        languages = LanguageSerializer(languages,many=True)
        return Response(languages.data)
    def put(self, request, id:int):
        try:
            language = Language.objects.get(id=id)
            serializer = LanguageSerializer(data=language)
            return Response(serializer.data)
        except:
            return Response({'Status':'Language not found'},status=status.HTTP_404_NOT_FOUND)

class GetPublisherView(APIView):
    def get(self, request):
        publishers = Publisher.objects.all()
        publishers = PublisherSerializer(publishers,many=True)
        return Response(publishers.data)
    def put(self, request, id: int):
        try:
            publisher = Publisher.objects.get(id=id)
            serializer = PublisherSerializer(data = publisher)
            return Response(serializer.data)
        except:
            return Response({'Status':'Publisher not found'}, status=status.HTTP_404_NOT_FOUND)

class GetBookView(APIView):
    """
        Get a book by id
    """
    def put(self, request,id:str):
        try:
            book = Book.objects.get(id=id)
            result = BookSerializer(book).data
            img = BookImage.objects.get(book=book)
            result['img_url'] = f'https://www.pythonanywhere.com/get/img/{img.id}'
            return Response(result)
        except:
            return Response({'Status':'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request):
        books = Book.objects.all()
        result = []
        i=0
        for book in books:  
            img = BookImage.objects.get(book=book)
            book = BookSerializer(book).data
            result.append(book)
            result[i]['img_url'] = f'https://www.pythonanywhere.com/get/img/{img.id}'
            i+=1
        return Response(result,status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        title = data.get('title', False)
        books_list = []
        if title:
            books = Book.objects.filter(title__icontains=title)
            for book in books:
                img = BookImage.objects.get(book=book)
                book1 = BookSerializer(book).data
                book1['img'] =f'https://www.pythonanywhere.com/get/img/{img.id}'
                books_list.append(book1)
            return Response(books_list)
        return Response({'Status':'title is required'},status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    """
        Update a book by id
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self,request,id:str):
        data = request.data
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book, data = data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Status":"Updated"},status=status.HTTP_200_OK)
            return Response({"Status":"No validation"},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status":"No validation"},status=status.HTTP_400_BAD_REQUEST)
    
    """
        Delete a book by id
    """
    def delete(self,request,id:str):
        try:
            book = Book.objects.get(id=id)
            img = BookImage.objects.get(book=book)
            book.delete()
            img.delete()
            return Response({"Status":"Deleted"},status=status.HTTP_200_OK)
        except:
            return Response({"Status":"Not found"},status=status.HTTP_404_NOT_FOUND)


class GetImageView(APIView):
    def get(self, request):
        images = BookImage.objects.all()
        image_list = []
        for image in images:
            data = BookImageSerializer(image).data
            data['img_url'] =f'https://www.pythonanywhere.com/get/img/{image.id}'
            image_list.append(data)
        return Response(image_list)


class SaveView(APIView):
    def get(self, request,id:int):
        img = BookImage.objects.get(id=id)
        img = img.image
        image = open(img.path,'rb')
        response = FileResponse(image)
        return response
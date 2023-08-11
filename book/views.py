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

from .models import BookImage,Book

class GenreView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request):
        print(request.user)
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
            token = Token.objects.get(user = user)
            return Response({'Status': 'OK','Token': token.key},status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'User not found', 'Token':None},status=status.HTTP_404_NOT_FOUND)
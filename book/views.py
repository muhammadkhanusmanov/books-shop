from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers.author_serializers import AuthorSerializer
from .serializers.genre_serializers import GenreSerializer
from .serializers.publisher_serializers import PublisherSerializer
from .serializers.language_serializers import LanguageSerializer
from .serializers.book_serializers import BookSerializer

class GenreView(APIView):
    def post(self, request):
        data = request.data
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class AuthorView(APIView):
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class PublisherView(APIView):
    def post(self,request):
        data = request.data
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

class LanguageView(APIView):
    def post(self,request):
        data = request.data
        serializer = LanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

class BookView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)

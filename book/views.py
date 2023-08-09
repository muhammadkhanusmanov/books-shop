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

class AddGenre(APIView):
    def post(self, request):
        data = request.data
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class AddAuthor(APIView):
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class AddPublisher(APIView):
    def post(self,request):
        data = request.data
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response({'Status': 'Bad Request'},status=status.HTTP_400_BAD_REQUEST)
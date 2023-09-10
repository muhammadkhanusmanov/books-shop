from rest_framework import serializers
from book.models import Book
from book.serializers.genre_serializers import GenreSerializer
from book.serializers.author_serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    
    publisher = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    genres = GenreSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
    
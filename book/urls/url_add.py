from django.urls import path
from ..views import (
    GenreView,
    AuthorView,
    PublisherView,
    LanguageView,
    BookView,
    BookImageView,
)

urlpatterns = [
    path('genre/', GenreView.as_view()),
    path('author/', AuthorView.as_view()),
    path('publisher/', PublisherView.as_view()),
    path('language/', LanguageView.as_view()),
    path('book/', BookView.as_view()),
    path('bookimage/', BookImageView.as_view()),
 
]
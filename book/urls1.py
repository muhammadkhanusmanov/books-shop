from django.urls import path
from .views import (
    GenreView,
    AuthorView,
    PublisherView,
    LanguageView,
    BookView
)

urlpatterns = [
    path('genre/', GenreView.as_view()),
    path('author/', AuthorView.as_view()),
    path('publisher/', PublisherView.as_view()),
    path('language/', LanguageView.as_view()),
    path('book/', BookView.ass_view()),
]
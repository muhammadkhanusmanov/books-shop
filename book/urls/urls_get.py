from django.urls import path
from ..views import (
    GetGenreView,
    GetAuthorView,
    GetBookView,
    GetImageView,
    GetLanguageView,
    GetPublisherView
    )
urlpatterns = [
    path('genres/',GetGenreView.as_view()),
    path('authors/',GetAuthorView.as_view()),
    path('books/',GetBookView.as_view()),
    path('images/',GetImageView.as_view()),
    path('languages/',GetLanguageView.as_view()),
    path('publishers/',GetPublisherView.as_view()),
]
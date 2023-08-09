from django.urls import path
from .views import (
    AddGenre,
    AddAuthor
)

urlpatterns = [
    path('genre/', AddGenre.as_view()),
    path('author/', AddAuthor.as_view()),
]
from django.urls import path
from .views import (
    AddGenre,
    AddAuthor,
    AddPublisher
)

urlpatterns = [
    path('genre/', AddGenre.as_view()),
    path('author/', AddAuthor.as_view()),
    path('publisher/', AddPublisher.as_view()),
]
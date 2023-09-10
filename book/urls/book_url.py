from django.urls import path
from ..views import (
    BookView,
    GetBookView
    )
urlpatterns = [
    path('delete/<str:id>',BookView.as_view()),
    path('update/<str:id>',BookView.as_view()),
    path('getbyid/<str:id>',GetBookView.as_view())
]
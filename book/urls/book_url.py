from django.urls import path
from ..views import (
    BookView
    )
urlpatterns = [
    path('delete/<str:id>',BookView.as_view()),
    path('update/<str:id>',BookView.as_view()),
]
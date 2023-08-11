from django.urls import path

from book.views import (
    UserView
    )


urlpatterns = [
    path('sign_in/',UserView.as_view()),
    path('sign_up/',UserView.as_view()),
]
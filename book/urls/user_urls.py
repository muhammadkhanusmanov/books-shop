from django.urls import path

from book.views import (
    UserView,
    LogOut
    )


urlpatterns = [
    path('sign_in/',UserView.as_view()),
    path('login/',UserView.as_view()),
    path('logout/',LogOut.as_view()),
]
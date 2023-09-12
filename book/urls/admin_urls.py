from django.urls import path
from ..views import (
    GenreView,
    AuthorView,
    PublisherView,
    LanguageView,
    BookView,
    BookImageView,
    CheckAdminView
)

urlpatterns = [
    path('addgenre/', GenreView.as_view()),
    path('addauthor/', AuthorView.as_view()),
    path('addpublisher/', PublisherView.as_view()),
    path('addlanguage/', LanguageView.as_view()),
    path('addbook/', BookView.as_view()),
    path('addbookimage/', BookImageView.as_view()),
    path('checkin/',CheckAdminView.as_view()),
    path('bookdelete/<str:id>',BookView.as_view()),
    path('bookupdate/<str:id>',BookView.as_view()),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', include('book.urls.url_add')),
    path('user/',include('book.urls.user_urls')),
    path('get/', include('book.urls.urls_get')),
]

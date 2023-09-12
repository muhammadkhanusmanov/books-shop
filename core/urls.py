from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', include('book.urls.admin_urls')),
    path('user/',include('book.urls.user_urls')),
    path('get/', include('book.urls.urls_get')),
]

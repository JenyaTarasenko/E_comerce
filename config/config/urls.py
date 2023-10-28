from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls', namespace='myapp')),#перенаправляет в приложение myapp
    path('users/', include('users.urls', namespace='users')),#перенаправляет в приложение users
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
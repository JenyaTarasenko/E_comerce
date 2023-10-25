from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls', namespace='myapp')),#include first app приложение myapp
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
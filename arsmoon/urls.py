from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('base.urls')),
    path('subscribes/', views.Subscribes.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

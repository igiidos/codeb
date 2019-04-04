from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('accounts/', include('accountsapp.urls')),
    path('cssapp/', include('cssapp.urls')),
    path('htmlapp/', include('htmlapp.urls')),
    path('jsapp/', include('jsapp.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("download/<str:filename>/", views.download_file, name="download_file"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

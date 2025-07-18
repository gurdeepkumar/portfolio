from django.shortcuts import render
from django.http import FileResponse, Http404
import os
from django.conf import settings


def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        response = FileResponse(
            open(file_path, "rb"), as_attachment=True, filename=filename
        )
        return response
    else:
        raise Http404("File does not exist")


def home(request):
    return render(request, "core/home.html")

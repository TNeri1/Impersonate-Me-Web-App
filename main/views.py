from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(response):
    if response.method == 'POST' and response.FILES['upload']:
        upload = response.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(response, 'main/index.html', {'file_url': file_url})
    return render(response, 'main/index.html')
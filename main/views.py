from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(response):
    if response.method == 'POST' and response.FILES['upload']:
        upload = response.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(response, 'main/upload.html', {'file_url': file_url})
    return render(response, 'main/upload.html')

def video_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'main/video_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'main/video_upload.html')
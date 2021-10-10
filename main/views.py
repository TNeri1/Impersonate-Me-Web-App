from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from PIL import Image

# Create your views here.

def index(response):
    if response.method == 'POST' and response.FILES['upload']:
        upload = response.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        try: 
            img = Image.open('.'+file_url) 
        except IOError:
            pass
        img = img.resize((512, 512))
        img.save('./media/newphoto.jpg', 'JPEG')
        return render(response, 'main/index.html', {'file_url': './media/newphoto.jpg'})
    return render(response, 'main/index.html')

def base(response):
    return render(response, 'main/base.html')

def video_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'main/video_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'main/video_upload.html')

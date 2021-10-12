from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_upload/', views.video_upload, name='video_upload'),
    path('base/', views.base, name='base'),
    path('showvideo/', views.showvideo, name="showvideo"),
]
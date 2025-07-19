from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('download', views.download, name='download'),
    path('upload', views.upload, name='upload'),

    path('download_image', views.download_image, name="download_image")
]  
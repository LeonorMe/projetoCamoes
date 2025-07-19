from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('lusiadas', views.lusiadas, name='lusiadas'),
    path('galeria', views.galeria, name='galeria'),
    path('cronologia', views.cronologia, name='cronologia'),
    path('dados_cronologia', views.dados_cronologia, name='dados_cronologia'),
    path('video', views.video, name='video'),
    path('literatura', views.literatura, name='literatura'),
    path('sobre', views.sobre, name='sobre'),
    
    path('subscribe/', views.subscribe, name='subscribe'),
    
    path('redirect-me', views.redirect_me, name="redirect-me"),
    #path('download_pdf', views.download_pdf, name="download_pdf"),
    #path('404', views.error, name='error'),
    
]  
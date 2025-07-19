from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

from .models import Lusiadas
from .models import Quote
from .models import Image
from .models import Video
from .models import Book
from .models import Subscribed
from .models import Event

from .forms import SubscribeForm
import re

import zipfile
import io
from django.http import FileResponse
#from reportlab.pdfgen import canvas
#import reportlab 

def index(request):
    quote = Quote.get_random_approved()
    image = Image.get_random_one_approved()
    
    txt = '"' + quote.content + '"'
    poem = re.split("/", txt)
    
    context = {
        'form_subs' : SubscribeForm(),
        'quote_content': poem,
        'quote_author': quote.author,
        'quote_book': quote.book,
        'image_url' : image.img.url,
    }
    
    return render(request, 'index.html', context)
    #return HttpResponse(template.render(context, request))

def lusiadas(request):
    if request.GET.get("id"):
        id = request.GET.get("id")
        l = Lusiadas.get_estrofe(id=id)
        id = int(id)
        id_back = id-1 if id > 0 else 0
        id_next = id+1 if id < Lusiadas.size() -1 else Lusiadas.size() -1
    else:
        l = Lusiadas.get_cover()
        id_back = str(0)
        id_next = str(1)
        
    estrofe_pt = re.split("/",  l.estrofe_pt)
    estrofe_en = re.split("/",  l.estrofe_en)
    estrofe_note = l.estrofe_note if l.estrofe_note != "" else "Não estão disponíveis notas para esta estrofe."
    
    context ={
        'form_subs' : SubscribeForm(),
        "estrofe_canto" : l.canto,
        "estrofe_id" : l.estrofe_id,
        "estrofe_pt" : estrofe_pt,
        "estrofe_en" : estrofe_en,
        "estrofe_note": estrofe_note,
        "estrofe_img": l.estrofe_img.url,
        "estrofe_id_back": id_back,
        "estrofe_id_next": id_next,
        "audio_pt" : l.audio_pt
    }
    return render(request, 'lusiadas.html', context)

def literatura(request):
    books = Book.get_approved()
    context = {
        'form_subs' : SubscribeForm(),
        'books': books,
    }
    return render(request, 'literatura.html', context)

def cronologia(request):
    events = Event.get_all()
    context = {
        'form_subs' : SubscribeForm(),
        'events': events,
    }
    return render(request, 'cronologia.html', context)

def dados_cronologia(request):
    year = request.GET.get("year")
    event = Event.get_from_year(year=year)
    context = {
        'form_subs' : SubscribeForm(),
        'e': event,
    }
    return render(request, 'dados_cronologia.html', context)

def video(request):
    videos = Video.get_approved_by_date()
    context = {
        'form_subs' : SubscribeForm(),
        'videos': videos,
    }
    return render(request, 'video.html', context)

def galeria(request):
    images = Image.get_random_all_approved()
    context = {
        'form_subs' : SubscribeForm(),
        'images': images,
    }
    return render(request, 'galeria.html', context)

def sobre(request):
    context = {
        'form_subs' : SubscribeForm(),
    }
    return render(request, 'sobre.html', context)

# --------------------------------------

#def error(request):
#    return render(request, '404.html')

#exemplo
#>>> reverse("admin:index", query=[("color", "blue"), ("color", 1), ("none", None)])
#'/admin/?color=blue&color=1&none=None'

def redirect_me(request):
    return redirect(reverse('lusiadas'))

# --------------------------------------

def subscribe(request):
    if request.method == 'POST':
        form_subs = SubscribeForm(request.POST)
        if form_subs.is_valid():
            form_subs.save()
            
            link = reverse('index')
            output = _("Obrigada por subscrever!")
            html = '<html lang="pt"><body><p>%s</p> <a href="%s">Voltar à página principal.</a></body></html>' %output %link
            return HttpResponse(html)
    else:
        form_subs = SubscribeForm(None)
    
    return redirect("index") 


'''
def contact(request):
    if request.method == 'POST':
        formS = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["info@example.com"]
            if cc_myself:
                recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect("/thanks/")
'''
# --------------------------------------

'''
def translate(language):
    cur_lan = get_language()
    try:
        activate(language)
        text = _('hello')
    finally:
        activate(cur_lan)
    return text
'''
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from mainPages.models import Image

from .forms import UserUpdate
from .forms import QuoteUpload
from .forms import ImageUpload

import re

from django.core.mail import send_mail

import zipfile
import io
from django.http import FileResponse


@login_required(login_url='login')
def profile(request):
    
    if request.method == 'POST': 
        if 'submit_form_user' in request.POST:
            form_user = QuoteUpload(request.POST, prefix='form_user')
            if form_user.is_valid():
                form_user.save()
                messages.success(request, 'User information updated successfully.')
    
    context = {
        'form_user': UserUpdate(prefix='form_user'),
        }
    
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def download(request):
    # management_form 
    # messages.success(request, 'Quote submitted successfully.')
    if request.method == 'POST':    
        if 'download_form_estrofe' in request.POST:
            form_quote = QuoteUpload(request.POST, prefix='form_quote')
            if form_quote.is_valid():
                form_quote.save()
                messages.add_message(request, messages.SUCCESS, 'Quote submitted successfully.')
                #return redirect('dashboard_contrib')
        elif 'download_form_img' in request.POST:
            form_img = ImageUpload(request.POST, prefix='form_img')
            if form_img.is_valid():
                form_img.save()
                #return redirect('dashboard_contrib')
        #elif 'submit_form_book' in request.POST:
            
    
    images = Image.get_approved()
    #images_url = []
    #for i in images:
    #    images_url.append(re.split("/", i.img.url)[-1])
    
    context = {
        'images': images
        }
    
    return render(request, 'download.html', context)

@login_required(login_url='login')
def download_image(request):
    if request.method == 'POST':
        #with zipfile.ZipFile('images-download-camoes500anos.zip', 'x') as imgzip:
        #    imgzip.write('i.id.url')
        return redirect('dashboard')
    return redirect('dashboard')

''' Download pdf
def download_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="canto_estrofe.pdf")
'''

@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':  
        
        if 'submit_form_quote' in request.POST:
            form_quote = QuoteUpload(request.POST, prefix='form_quote')
            if form_quote.is_valid():
                form_quote.save()
                messages.success(request, 'Quote submitted successfully.')
                
        elif 'submit_form_img' in request.POST:
            form_img = ImageUpload(request.POST, prefix='form_img')
            if form_img.is_valid():
                form_img.save()
                messages.success(request, 'Image submitted successfully.')
    
    context = {
        'form_quote': QuoteUpload(prefix='form_quote'),
        'form_img': ImageUpload(prefix='form_img'),
        'form_user': UserUpdate(prefix='form_user'),
        }
    
    return render(request, 'upload.html', context)


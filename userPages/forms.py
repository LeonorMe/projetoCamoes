from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date

from mainPages.models import Image
from mainPages.models import Quote

class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class QuoteUpload(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['content', 'author', 'book']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['img', 'author', 'title','canto']

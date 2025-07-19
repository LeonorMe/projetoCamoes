from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date

from .models import Subscribed

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribed
        fields =  '__all__'
    
    def clean(self):
        super(SubscribeForm, self).clean()
        
        email = self.cleaned_data.get('email')
        
        if len(email) < 3:
            self._errors['username'] = self.error_class(['Email must be at least 3 characters long.'])
            # TODO validar se é um email novo - unique=True
        return self.cleaned_data

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

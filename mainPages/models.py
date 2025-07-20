from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator

import random
from datetime import date


# Create your models here.

class Subscribed(models.Model):
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "Subscribed"

    def __str__(self):
        return self.email

class Quote(models.Model):
    
    STATUS = {
        "OK" : "Public, aproved!",
        "Waiting" : "Private, waiting for aproval..."
    }
    
    content = models.TextField(max_length=500)
    author = models.CharField(max_length=100)
    book = models.CharField(max_length=100, blank=True)
    status = models.CharField(choices=STATUS, default="Waiting")
    
    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return f"({self.status}) {self.author} - {self.content}"
    
    def get_random():
        return Quote.objects.order_by("?").first()
    
    def get_random_approved():
        return Quote.objects.filter(status='OK').order_by("?").first()
    
    def get_random_quickly():
        max_id = Quote.objects.all().count()
        while True:
            pk = random.randint(1, max_id)
            category = Quote.objects.filter(pk=pk).first()
            if category:
                return category

class Lusiadas(models.Model):
    CANTO = {
    "I": "I",
    "II": "II",
    "III": "III",
    "IV": "IV",
    "V": "V",
    "VI": "VI",
    "VII": "VII",
    "VIII": "VIII",
    "IX": "IX",
    "X": "X"
    }
    
    canto = models.CharField(choices=CANTO, default=CANTO.get('I'))
    estrofe_id = models.CharField(max_length=4)
    estrofe_pt = models.TextField(max_length=500)
    estrofe_en = models.TextField(max_length=500, blank=True)
    estrofe_note = models.TextField(max_length=500, blank=True)
    estrofe_img = models.ImageField(default='fallback.jpg', blank=True)
    audio_pt = models.FileField(blank=True)
    
    class Meta:
        verbose_name_plural = "Os Lusíadas"
    
    def __str__(self):
        return f"Canto {self.canto}: ({self.estrofe_id}) {self.estrofe_pt}"
    
    def get_cover():
        return Lusiadas.objects.all().get(estrofe_id=0)
    
    def get_estrofe(id=1):
        return Lusiadas.objects.all().get(estrofe_id=id)
    
    def size():
        return int(Lusiadas.objects.all().count())

class Image(models.Model):
    CANTO = {
    "I": "I",
    "II": "II",
    "III": "III",
    "IV": "IV",
    "V": "V",
    "VI": "VI",
    "VII": "VII",
    "VIII": "VIII",
    "IX": "IX",
    "X": "X"
    }
    STATUS = {
        "OK" : "Public, aproved!",
        "Waiting" : "Private, waiting for aproval..."
    }
    
    img = models.ImageField(default='fallback.jpg')
    author = models.CharField(max_length=100, default="Anonymous")
    title = models.CharField(max_length=100, blank=True)
    canto = models.CharField(choices=CANTO, blank=True)
    alt = models.CharField(max_length=100, blank=True, default="Image from workshop")
    date = models.DateField(date.today, blank=True)
    status = models.CharField(choices=STATUS, default="Waiting")
    
    class Meta:
        verbose_name_plural = "Images"
        
    def __str__(self):
        return f"{self.status} {self.author} {self.img}"
    
    def get_approved():
        return Image.objects.filter(status='OK')
    
    def get_random_all_approved():
        return Image.objects.filter(status='OK').order_by("?")
    
    def get_random_one_approved():
        return Image.objects.filter(status='OK').order_by("?").first()

class Video(models.Model):
    STATUS = {
        "OK" : "Public, aproved!",
        "Waiting" : "Private, waiting for aproval..."
    }
    
    video = models.URLField(max_length = 200)
    title = models.CharField(max_length=100)
    img = models.ImageField(default='fallback.jpg')
    alt = models.CharField(max_length=100, blank=True, default="Capa do vídeo")
    ogdate = models.DateField(blank=True, default=date.today)
    author = models.CharField(max_length=100, blank=True, default="Anonymous")
    date = models.DateField(date.today, blank=True)
    status = models.CharField(choices=STATUS, default="Waiting")
    
    class Meta:
        verbose_name_plural = "Videos"
        
    def __str__(self):
        return f"({self.status}) {self.title} - {self.video}"
    
    def get_approved_by_date():
        return Video.objects.filter(status='OK').order_by('-ogdate')

class Book(models.Model):
    STATUS = {
        "OK" : "Public, aproved!",
        "Waiting" : "Private, waiting for aproval..."
    }
    
    url = models.URLField(max_length = 200)
    img = models.ImageField(default='fallback.jpg')
    alt = models.CharField(max_length=100, blank=True, default="Capa do PDF")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, default="Anonymous")
    ogdate = models.DateField(blank=True, default=date.today)
    status = models.CharField(choices=STATUS, default="Waiting", blank=True)
    
    class Meta:
        verbose_name_plural = "Books"
        
    def __str__(self):
        return f"{self.status}: {self.title} - {self.author}"
    
    def get_approved():
        return Book.objects.filter(status='OK').order_by('title', 'author', '-ogdate')

class Event(models.Model):
    year = models.PositiveIntegerField(default=1500, validators=[MinValueValidator(1300), MaxValueValidator(2200)])
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=150)
    content = models.TextField(max_length=500, blank=True)
    img = models.ImageField(default='fallback.jpg')
    
    class Meta:
        verbose_name_plural = "Events"
        
    def __str__(self):
        return f"{self.year} - {self.title}: {self.summary}"
    
    def get_all():
        return Event.objects.order_by('year')
    
    def get_from_year(year=1524):
        return Event.objects.get(year=year)
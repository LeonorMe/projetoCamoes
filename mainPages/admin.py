from django.contrib import admin

from .models import Subscribed
from .models import Lusiadas
from .models import Quote
from .models import Image
from .models import Video
from .models import Book
from .models import Event
# Register your models here.

# admin.site.register(nomeClasse)
admin.site.register(Subscribed)
admin.site.register(Lusiadas)
admin.site.register(Quote)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Book)
admin.site.register(Event)
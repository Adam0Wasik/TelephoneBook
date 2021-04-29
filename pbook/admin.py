from django.contrib import admin

# Register your models here.
from django.contrib import admin

from pbook.models import Osoba, Telefon, Email

admin.site.register(Osoba)
admin.site.register(Telefon)
admin.site.register(Email)

from django.http import HttpResponse, HttpResponseRedirect
from django.middleware import http
from django.shortcuts import render

from pbook.forms import AddForm, SearchForm, AddNumberForm, AddEmailForm

from pbook.models import Osoba, Telefon, Email


def index(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                number = form.cleaned_data['number']
                email = form.cleaned_data['email']

                person = Osoba(imie=name, nazwisko=surname)
                person.save()
                if number != "":
                    tel = Telefon(osoba=person, telefon=number)
                    tel.save()
                if email != "":
                    email = Email(osoba=person, email=email)
                    email.save()
                #clears form
                form = AddForm()

    osobaList = Osoba.objects.all()
    telefonList = Telefon.objects.all()
    emailList = Email.objects.all()
    #creating sub lists with only Osoba objects from 2d lists to check if osoba have email or number provided
    telefonExistList = []
    emailExistList = []
    for tel in telefonList:
        telefonExistList.append(tel.osoba)

    for em in emailList:
        emailExistList.append(em.osoba)

    return render(request, "index.html", { 'form' : form, 'osobaList' : osobaList, 'telefonList' : telefonList ,'emailList' : emailList, 'telefonExistList' : telefonExistList, 'emailExistList' : emailExistList, })

def search(request):
    form = SearchForm()
    return render(request, "search.html", {'form': form, })

def addNumber(request):
    form = AddNumberForm()
    return render(request, "addNumber.html", {'form': form, })

def addEmail(request):
    form = AddEmailForm()
    return render(request, "addEmail.html", {'form': form, })


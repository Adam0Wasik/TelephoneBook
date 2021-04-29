from django.http import HttpResponse, HttpResponseRedirect
from django.middleware import http
from django.shortcuts import render, redirect

from pbook.forms import AddForm, SearchForm, AddNumberForm, AddEmailForm, EditForm

from pbook.models import Osoba, Telefon, Email


def index(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)

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
    osobaList = Osoba.objects.all()
    telefonList = Telefon.objects.all()
    emailList = Email.objects.all()
    telefonExistList = []
    emailExistList = []
    for tel in telefonList:
        telefonExistList.append(tel.osoba)

    for em in emailList:
        emailExistList.append(em.osoba)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']

            idList = []
            #Nie do końca byłem pewien jaka logikę zastosowac do wyszukiwania
            for os in osobaList:
                if os.imie == name or os.nazwisko == surname:
                    idList.append(os.id)
            for em in emailList:
                if em.email == email:
                    idList.append(em.osoba.id)
            for tel in telefonList:
                if tel.telefon == number:
                    idList.append(em.osoba.id)
            #finally filter procces
            osobaList = Osoba.objects.filter(id__in=idList)
    return render(request, "search.html", {'form': form, 'osobaList' : osobaList, 'telefonList' : telefonList ,'emailList' : emailList, 'telefonExistList' : telefonExistList, 'emailExistList' : emailExistList,})

def addNumber(request, osid):
    form = AddNumberForm()
    person = Osoba.objects.get(id=osid)
    telefonList = Telefon.objects.all()
    if request.method == 'POST':
        form = AddNumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            tel = Telefon(osoba=person, telefon=number)
            tel.save()
    return render(request, "addNumber.html", {'form': form, 'osoba' : person, 'telefonList' : telefonList , })

def addEmail(request, osid):
    form = AddEmailForm()
    person = Osoba.objects.get(id=osid)
    emailList = Email.objects.all()
    if request.method == 'POST':
        form = AddEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email = Email(osoba=person, email=email)
            email.save()
    return render(request, "addEmail.html", {'form': form, 'osoba' : person, 'emailList' : emailList, })

def delete(request, osid):
    Osoba.objects.filter(id=osid).delete()
    return redirect("/")

def edit(request, osid):
    person = Osoba.objects.get(id=osid)
    form = EditForm(initial = {'name': person.imie, 'surname' : person.nazwisko})
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            person.imie = name
            person.nazwisk = surname
            person.save()
            return redirect("/")
    return render(request, "edit.html", {'form': form, })


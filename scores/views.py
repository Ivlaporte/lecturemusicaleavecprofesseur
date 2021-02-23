from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
#from pdf2image import convert_from_path

from .models import MusicScore

links = [{'Niveau_1':1, 'Niveau_2':2, 'Niveau_3':3},
    {'Niveau_1':4, 'Niveau_2':5, 'Niveau_3':6},
    {'Niveau_1':4, 'Niveau_2':50, 'Niveau_3':60},]

def index(request): #, year, month):
#    return render(request, 'menu.html') # hors devient sers-pu-à-rien
    # year = int(year)
    # month = int(month)
    # if year < 2000 or year > 2099: year = date.today().year
    # month_name = calendar.month_name[month]
    # tit = "La plus belle année %s %s" % (month_name, year)
    # cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse('<h1>%s</h1><p>%s</p>' % (tit, cal))
    
    return render(request, 'accueil/1accueil.html', {'links': links})

def introLMAP(request):
    
    return render(request, 'accueil/2introduction.html', {'links': links})
def show_level(request, level):
    M_Scor = MusicScore.objects.filter(readlevel__equals = level)

    return HttpResponse(M_Scor, content_type='text/plain')
def partitions(request):
    # t = date.today()
    # annee = t.year
    return render(request, 'partitions/partitions.html', {'links': links})
def partNiv1(request):
    return render(request, 'partitions/partNiv1.html', {'links': links})
def partNiv2a(request):
    return render(request, 'partitions/partNiv2a.html', {'links': links})
def partNiv3a(request):
    return render(request, 'partitions/partNiv3a.html', {'links': links})
def gammes(request):
    return render(request, 'partitions/3gammeReM.html', {'links': links})
def methode(request):

    return render(request, 'accueil/3methodeseesse.html', {'links': links})
def contactLMAP(request):
    return render(request, 'contact/contactLMAP.html', {'links': links})

def home(request):
    return render(request, '././template/home.html')
def inexistant(request):
    return render(request, 'accueil/inexistant.html')
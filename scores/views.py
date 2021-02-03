from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
#from pdf2image import convert_from_path


def index(request): #, year, month):
#    return render(request, 'menu.html') # hors devient sers-pu-à-rien
    # year = int(year)
    # month = int(month)
    # if year < 2000 or year > 2099: year = date.today().year
    # month_name = calendar.month_name[month]
    # tit = "La plus belle année %s %s" % (month_name, year)
    # cal = HTMLCalendar().formatmonth(year, month)
    # return HttpResponse('<h1>%s</h1><p>%s</p>' % (tit, cal))
    return render(request, 'accueil/1accueil.html')

def introLMAP(request):
    return render(request, 'accueil/2introduction.html')
def partitions(request):
    # t = date.today()
    # annee = t.year
    return render(request, 'partitions/partitions.html')
def partNiv1(request):
    return render(request, 'partitions/partNiv1.html')
def partNiv2a(request):
    return render(request, 'partitions/partNiv2a.html')
def partNiv3a(request):
    return render(request, 'partitions/partNiv3a.html')
def gammes(request):
    return render(request, 'partitions/3gammeReM.html')
def methode(request):
    return render(request, 'accueil/3methodeseesse.html')
def contactLMAP(request):
    return render(request, 'contact/contactLMAP.html')

def home(request):
    return render(request, '././template/home.html')
def inexistant(request):
    return render(request, 'accueil/inexistant.html')


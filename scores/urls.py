from django.urls import path
from . import views

app_name = 'partitions'
urlpatterns = [
    path('introduction/', views.introLMAP, name='introLMAP'),
    path('partitions/', views.partitions, name='partitions'),
    path('partNiv1/', views.partNiv1, name='partNiv1'),
    path('partNiv2a/', views.partNiv2a, name='partNiv2a'),
    path('partNiv3a/', views.partNiv3a, name='partNiv3a'),
    path('gammes/', views.gammes, name='gammes'),
    path('methode/', views.methode, name='methode'),
    path('contactLMAP/', views.contactLMAP, name='contactLMAP'),
    path('inexistant/', views.inexistant, name='inexistant'),
    path('', views.index, name='index'),
]
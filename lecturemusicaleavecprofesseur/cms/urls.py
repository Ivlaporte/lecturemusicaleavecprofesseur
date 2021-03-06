from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('home/', views.home, name='cmsHome'),
]
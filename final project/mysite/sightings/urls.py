from . import views
from django.urls import path

app_name = 'sightings'

urlpatterns = [
    path('', views.list, name='list'),
    path('stats/',views.stats, name='stats'),
    path('add/',views.add, name='add'),
    path('<str:idd>/',views.update, name='update'), 
]
#    path('<str:usi>/',views.delete, name='delete'),
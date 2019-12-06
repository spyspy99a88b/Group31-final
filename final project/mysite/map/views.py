from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from sightings.models import squirrel


def index(request):
    sightings = squirrel.objects.all()
    context= {'sightings':sightings}
    return render(request, 'map/map.html',context)




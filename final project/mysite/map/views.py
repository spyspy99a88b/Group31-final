from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from sightings.models import Squirrel


def index(request):
    sightings = Squirrel.objects.all()[:100]
    context= {'sightings':sightings}
    return render(request, 'map/map.html',context)




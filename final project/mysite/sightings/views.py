from django.shortcuts import render
from django.shortcuts import render
from .models import squirrel

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


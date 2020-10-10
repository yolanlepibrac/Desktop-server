import requests
from django.shortcuts import render
from django.http import HttpResponse

import os

from .models import Notes

def index(request):
    return HttpResponse("Hello, world.")

def detail(request, note_id):
    return HttpResponse("You're looking at question %s." % note_id)

def getTitles(request):
    notes = Notes.objects.order_by('-title')[:5]
    output = ', '.join([n.title for n in notes])
    return HttpResponse(output)

def teapot(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def timeEnv(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

from .models import Notes


@csrf_exempt
def getNotes(request):
    notes = Notes.objects.order_by('-title')[:5]
    output = ', '.join([n.title for n in notes])
    return HttpResponse(output)


def createNote(request):
    print(request)
    newNote = Notes.objects.create(title="new notes 00", value="ma value a moi")
    print(newNote)
    newNote.save()
    # entry.notes.add(newNote)
    return HttpResponse("note inserted")




def index(request):
    return HttpResponse("Hello, world.")

def detail(request, note_id):
    return HttpResponse("You're looking at question %s." % note_id)

def teapot(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def timeEnv(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)
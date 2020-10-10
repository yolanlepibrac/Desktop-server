from django.shortcuts import render
from django.http import HttpResponse

from .models import Notes

def index(request):
    return HttpResponse("Hello, world.")

def detail(request, note_id):
    return HttpResponse("You're looking at question %s." % note_id)

def getTitles(request):
    notes = Notes.objects.order_by('-title')[:5]
    output = ', '.join([n.title for n in notes])
    return HttpResponse(output)
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from .serializers import  NoteSerializer, UserSerializer
from .models import Note


def notes_get(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def note_create(request):
    data = JSONParser().parse(request)
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def note_update(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    data = JSONParser().parse(request)
    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


def note_delete(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    note.delete()
    return HttpResponse(status=204)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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
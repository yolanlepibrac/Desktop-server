from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teapot/', views.teapot, name='teapot'),
    path('<str:note_id>/detail/', views.detail, name='note_detail'),
    path('timeEnv/', views.timeEnv, name='timeEnv'),
    path('notes/get/all', views.getNotes, name='getNotes'),
    path('notes/create/', views.createNote, name='createNote'),
]
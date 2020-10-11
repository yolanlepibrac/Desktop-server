from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teapot/', views.teapot, name='teapot'),
    path('<str:note_id>/detail/', views.detail, name='note_detail'),
    path('timeEnv/', views.timeEnv, name='timeEnv'),
    path('notes/get/all', views.notes_get, name='getNotes'),
    path('notes/create', views.note_create, name='createNote'),
    path('notes/update/<int:id>', views.note_update, name='updateNote'),
    path('notes/delete/<int:id>', views.note_delete, name='deleteNote'),
]
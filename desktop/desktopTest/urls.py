from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('<str:note_id>/detail/', views.detail, name='note_detail'),
    path('titles', views.getTitles, name='getTitles'),
]
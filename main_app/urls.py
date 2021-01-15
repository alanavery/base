from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms_index, name='rooms_index')
]

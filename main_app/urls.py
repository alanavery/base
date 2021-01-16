from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms_index, name='rooms_index'),
    path('rooms/<int:room_id>/', views.rooms_details, name='rooms_details'),
    path('rooms/create/', views.RoomCreate.as_view(), name='rooms_create'),
    path('rooms/<int:pk>/update/',
         views.RoomUpdate.as_view(), name='rooms_update'),
    path('rooms/<int:pk>/delete/',
         views.RoomDelete.as_view(), name='rooms_delete'),
]

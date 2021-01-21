from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('user/<username>/', views.profile, name='profile'),
    path('bookings/', views.bookings_index, name='bookings_index'),
    path('bookings/<int:booking_id>/',
         views.bookings_details, name='bookings_details'),
    path('bookings/create/', views.BookingCreate.as_view(), name='bookings_create'),
    path('bookings/<int:pk>/update/',
         views.BookingUpdate.as_view(), name='bookings_update'),
    path('bookings/<int:pk>/delete/',
         views.BookingDelete.as_view(), name='bookings_delete'),
]

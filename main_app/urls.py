from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('bookings/', views.bookings_index, name='bookings_index'),
    path('bookings/<int:booking_id>/',
         views.bookings_details, name='bookings_details'),
    path('bookings/<int:pk>/update/',
         views.BookingUpdate.as_view(), name='bookings_update'),
    path('bookings/<int:pk>/delete/',
         views.BookingDelete.as_view(), name='bookings_delete'),
    path('book/', views.book, name='book'),
    path('book/<int:room_number>/', views.book_guest_details, name='book_guest_details'),
#     path('book/guest_details', views.CreateBooking.as_view(), name='bookings_create'),
]

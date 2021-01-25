from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('book/', views.book, name='book'),
    path('book/<int:room_number>/', views.create_booking, name='create_booking'),
    path('book/confirmation/<int:booking_id>/', views.book_confirmation, name='book_confirmation'),
]

# path('bookings/', views.bookings_index, name='bookings_index'),
# path('bookings/<int:booking_id>/', views.bookings_details, name='bookings_details'),
# path('bookings/<int:pk>/update/', views.BookingUpdate.as_view(), name='bookings_update'),
# path('bookings/<int:pk>/delete/', views.BookingDelete.as_view(), name='bookings_delete'),

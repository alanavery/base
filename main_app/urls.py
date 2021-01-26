from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update_user', views.update_user, name='update_user'),
    path('profile/update_guest', views.update_guest, name='update_guest'),
    path('book/', views.book, name='book'),
    path('book/<int:room_number>/', views.create_booking, name='create_booking'),
    path('book/confirmation/<int:booking_id>/',
         views.book_confirmation, name='book_confirmation'),
]

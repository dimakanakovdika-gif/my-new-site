from django.urls import path
from . import views
from . import auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('masters/', views.masters, name='masters'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reviews/', views.reviews, name='reviews'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('add_review/', views.add_review, name='add_review'),
    path('profile/', views.profile, name='profile'),
    path('chat/', views.chat, name='chat'),
    path('login/', auth_views.login_view, name='login'),
    path('register/', auth_views.register_view, name='register'),
    path('logout/', auth_views.logout_view, name='logout'),
path('faq/', views.faq_view, name='faq'),
    path('game/', views.game_view, name='game'), 
    
]
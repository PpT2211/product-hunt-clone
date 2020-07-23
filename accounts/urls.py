from django.urls import path
from . import views

urlpatterns = [
    path('Sign-Up/', views.signUp, name='signup'),
    path('Login/', views.login, name='login'),
    path('Logout/', views.logout, name='logout')
]

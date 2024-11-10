# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('health_data/', views.health_data, name='health_data'),
    path('visualization/', views.data_visualization, name='visualization'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage with login and signup options
    path('health_data/', views.health_data, name='health_data'),  # Data input view
    path('visualization/', views.data_visualization, name='data_visualization'),  # Data visualization view
    path('logout/', views.logout_view, name='logout'),  # Logout view
]

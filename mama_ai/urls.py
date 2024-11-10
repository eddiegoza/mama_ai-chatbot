# mama_ai/urls.py

from django.contrib import admin
from django.urls import path, include
from ai.views import chat  # Import the chat view directly
from users import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # User routes
    path('ai/', include('ai.urls')),  # AI routes
    path('', chat, name='home'),  # Map the root URL to the chat view
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('health_data/', views.health_data, name='health_data'),
    path('visualization/', views.data_visualization, name='visualization'),
] 

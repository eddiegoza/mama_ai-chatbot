# mama_ai/urls.py

from django.contrib import admin
from django.urls import path, include
from ai.views import chat  # Import the chat view directly
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User routes
    path('users/', include('users.urls')),  # Include all routes from users/urls.py
    
    # AI routes
    path('ai/', include('ai.urls')),  # Include all routes from ai/urls.py
    path('ai/chat/', chat, name='chat'),  # Direct chat route
    
    # Home, login, register, and health data routes (from users/views.py)
    path('', views.home, name='home'),  # Home page as root URL
    path('register/', views.home, name='register'),  # Registration handled in home view
    path('login/', views.home, name='login'),  # Login handled in home view
    
    # Health data and visualization views
    path('health_data/', views.health_data, name='health_data'),
    path('visualization/', views.data_visualization, name='visualization'),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

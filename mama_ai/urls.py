# mama_ai/urls.py

from django.contrib import admin
from django.urls import path, include
from ai.views import chat  # Import the chat view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # User routes
    path('ai/', include('ai.urls')),  # AI routes
    path('', chat, name='home'),  # Map the root URL to the chat view
]

# ai/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .services import get_ai_response  # We will define this service

def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = get_ai_response(user_message)  # Call AI service
        return JsonResponse({'message': bot_response})
    return render(request, 'ai/chatbot.html')

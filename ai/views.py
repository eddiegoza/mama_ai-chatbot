# # ai/views.py

# from django.shortcuts import render
# from django.http import JsonResponse
# from .services import get_ai_response  # We will define this service


# def chat(request):
#     if request.method == 'POST':
#         user_message = request.POST.get('message')
#         bot_response = get_ai_response(user_message)  # Call AI service
#         return JsonResponse({'message': bot_response})
#     return render(request, 'ai/chatbot.html')

# ai/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .services import get_ai_response  # AI service to handle user messages

def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()
        if user_message:
            try:
                bot_response = get_ai_response(user_message)  # Get response from AI service
                return JsonResponse({'message': bot_response}, status=200)
            except Exception as e:
                # Log the error for debugging (if logging is set up)
                print(f"Error processing AI response: {e}")
                return JsonResponse({'message': 'Sorry, an error occurred while processing your message.'}, status=500)
        return JsonResponse({'message': 'Message cannot be empty.'}, status=400)
    
    # Render the chatbot interface for GET requests
    return render(request, 'ai/chatbot.html')

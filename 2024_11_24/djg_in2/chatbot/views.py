from django.shortcuts import render

# Create your views here.
import openai
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

@api_view(['POST'])
def chat_with_gpt(request):
    try:
        user_message = request.data.get('message', '')

        if not user_message:
            return JsonResponse({'error': 'Message is required'}, status=400)

        # OpenAI API 호출
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 사용할 모델 지정
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']

        return JsonResponse({'message': bot_reply}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
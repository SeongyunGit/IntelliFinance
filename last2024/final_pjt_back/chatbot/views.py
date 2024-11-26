from django.shortcuts import render

# Create your views here.
import openai
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from Open_API.models import IntegrationProduct


openai.api_key = settings.OPENAI_API_KEY

@api_view(['POST'])
def chat_with_gpt(request):
    try:
        user_message = request.data.get('message', '')

        if not user_message:
            return JsonResponse({'error': 'Message is required'}, status=400)

        products_context = IntegrationProduct.objects.all()
        # OpenAI API 호출
        
        products_text = ""
        for product in products_context:
            loan_lmt = str(product.loan_lmt).replace('"', "'") if product.loan_lmt else "정보 없음"
            
            products_text += f"""
            금융회사: {product.kor_co_nm},상품명: {product.fin_prdt_nm},상품유형: {product.type_a},가입방법: {product.join_way},만기후이자: {product.mtrt_int},가입대상: {product.join_member},대출인지세: {product.loan_inci_expn},조기상환수수료: {product.erly_rpay_fee},연체금리: {product.dly_rate},대출한도: {product.loan_lmt}"""

        print(products_text)
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # 사용할 모델 지정
            messages=[
                {"role": "system", "content": f"""You are a financial product expert. Your task is to provide expert advice based on the following real-time financial product data:
                
                {products_text}
                
                Provide recommendations only from these actual products. Keep the response under 50 words."""},
                {"role":"user", "content": user_message}
                ]
        )
        bot_reply = response['choices'][0]['message']['content']

        return JsonResponse({'message': bot_reply}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
from ast import Try
import requests
from .models import CurrencyExchange
from .serializers import CurrencyExchangeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from django.conf import settings

@api_view(['POST'])
def fetch_and_save_exchange_rates(request):
    # 오늘 날짜로 이미 데이터가 있는지 확인
    # if CurrencyExchange.objects.filter(updated_at__date=timezone.now().date()).exists():
    #     # 데이터가 존재하면 바로 반환
    #     exchange_rates = CurrencyExchange.objects.all()
    #     serializer = CurrencyExchangeSerializer(exchange_rates, many=True)
    #     return Response(serializer.data)
    
    # 오늘 날짜를 yyyyMMdd 형식으로 설정
    # today = timezone.now().strftime("%Y%m%d")

    # 요청 URL과 파라미터 설정
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"

    # 기본 파라미터 설정
    params = {
        "authkey": settings.EXCHANGE_API_KEY,  # 인증키
        # "searchdate": '20241125',  # 오늘 날짜를 yyyyMMdd 형식으로 설정
        "data": "AP01",  # 환율 데이터
    }

    # exchange_rates = CurrencyExchange.objects.all()
    # if exchange_rates:  # 데이터가 없을 경우
    #     # 저장되어 있는 데이터 반환
    #     serializer = CurrencyExchangeSerializer(exchange_rates, many=True)
    #     return Response(serializer.data)

    # API로부터 데이터 가져오기
    # try:
    response = requests.get(url, params=params, verify=False)
    data = response.json()
    # except 
    if data == []:  # 데이터가 없을 경우
        # 저장되어 있는 데이터 반환
        serializer = CurrencyExchangeSerializer(exchange_rates, many=True)
        return Response(serializer.data)


    # 환율 데이터를 하나씩 처리
    for entry in data:
        result = entry.get("result")
        if result == 1:
            cur_unit = entry.get("cur_unit")
            cur_nm = entry.get("cur_nm")
            ttb = entry.get("ttb")
            tts = entry.get("tts")
            deal_bas_r = entry.get("deal_bas_r")
            bkpr = entry.get("bkpr")
            yy_efee_r = entry.get("yy_efee_r")
            ten_dd_efee_r = entry.get("ten_dd_efee_r")
            kftc_deal_bas_r = entry.get("kftc_deal_bas_r")
            kftc_bkpr = entry.get("kftc_bkpr")

            # 데이터를 업데이트하거나 새로 생성
            currency, created = CurrencyExchange.objects.update_or_create(
                cur_unit=cur_unit,  # 통화 단위로 고유 식별
                defaults={
                    "result": result,
                    "cur_nm": cur_nm,
                    "ttb": ttb,
                    "tts": tts,
                    "deal_bas_r": deal_bas_r,
                    "bkpr": bkpr,
                    "yy_efee_r": yy_efee_r,
                    "ten_dd_efee_r": ten_dd_efee_r,
                    "kftc_deal_bas_r": kftc_deal_bas_r,
                    "kftc_bkpr": kftc_bkpr,
                    # "updated_at": timezone.now(),  # 업데이트 날짜 자동으로 추가
                }
            )

    # 저장된 데이터를 반환 (새로 추가된 또는 업데이트된 데이터)
    exchange_rates = CurrencyExchange.objects.all()
    serializer = CurrencyExchangeSerializer(exchange_rates, many=True)
    return Response(serializer.data)

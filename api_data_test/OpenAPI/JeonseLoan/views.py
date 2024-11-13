import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import LoanProduct, LoanProductOption
from datetime import datetime
from django.conf import settings

@api_view(['GET'])
def JeonseLoan(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '050000',
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 데이터베이스에 저장
        for item in base_list:
            # LoanProduct 저장
            loan_product = LoanProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                loan_inci_expn=item['loan_inci_expn'],
                erly_rpay_fee=item['erly_rpay_fee'],
                dly_rate=item['dly_rate'],
                loan_lmt=item['loan_lmt'],
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d'),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d') if item.get('dcls_end_day') else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # LoanProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    LoanProductOption.objects.create(
                        loan_product=loan_product,
                        rpay_type=option['rpay_type'],
                        rpay_type_nm=option['rpay_type_nm'],
                        lend_rate_type=option['lend_rate_type'],
                        lend_rate_type_nm=option['lend_rate_type_nm'],
                        lend_rate_min=option['lend_rate_min'],
                        lend_rate_max=option['lend_rate_max'],
                        lend_rate_avg=option['lend_rate_avg']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

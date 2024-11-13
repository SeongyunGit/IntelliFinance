import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import DepositProduct, DepositProductOption
from datetime import datetime
from django.conf import settings

@api_view(['GET'])
def PensionSavings(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '060000',
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
            # DepositProduct 저장
            product = DepositProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                prdt_type=item['prdt_type'],
                prdt_type_nm=item['prdt_type_nm'],
                avg_prft_rate=item['avg_prft_rate'],
                btrm_prft_rate_1=item['btrm_prft_rate_1'],
                btrm_prft_rate_2=item.get('btrm_prft_rate_2', None),
                btrm_prft_rate_3=item.get('btrm_prft_rate_3', None),
                sale_co=item['sale_co'],
                sale_strt_day=datetime.strptime(item['sale_strt_day'], '%Y%m%d') if item.get('sale_strt_day') else None,
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d'),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d') if item.get('dcls_end_day') else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # DepositProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    DepositProductOption.objects.create(
                        deposit_product=product,
                        dcls_month=option['dcls_month'],
                        fin_co_no=option['fin_co_no'],
                        fin_prdt_cd=option['fin_prdt_cd'],
                        pnsn_recp_trm=option['pnsn_recp_trm'],
                        pnsn_recp_trm_nm=option['pnsn_recp_trm_nm'],
                        pnsn_entr_age=option['pnsn_entr_age'],
                        pnsn_entr_age_nm=option['pnsn_entr_age_nm'],
                        mon_paym_atm=option['mon_paym_atm'],
                        mon_paym_atm_nm=option['mon_paym_atm_nm'],
                        paym_prd=option['paym_prd'],
                        paym_prd_nm=option['paym_prd_nm'],
                        pnsn_strt_age=option['pnsn_strt_age'],
                        pnsn_strt_age_nm=option['pnsn_strt_age_nm'],
                        pnsn_recp_amt=option['pnsn_recp_amt']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

import json
from django.shortcuts import render
from .models import FinancialProduct

def insert_financial_products(request):
    # JSON 데이터를 직접 가져옴 (여기서는 예시 데이터를 하드코딩)
    json_data = '''{
        "result": {
            "baseList": [
                {
                    "dcls_month": "201609",
                    "fin_co_no": "0010001",
                    "fin_prdt_cd": "WR0001A",
                    "kor_co_nm": "우리은행",
                    "fin_prdt_nm": "우리웰리치 주거래예금",
                    "join_way": "영업점,인터넷,스마트폰",
                    "mtrt_int": "만기 후\n- 1개월이내 : 만기시점약정이율×50%",
                    "spcl_cnd": "다음 중 하나 충족한 입금건에 대해 최고 연0.2%p",
                    "join_deny": "1",
                    "join_member": "실명의 개인",
                    "etc_note": "-추가입금은 신규가입 시 선택한 예치기간을 각 입금건별 입금일로부터 적용",
                    "max_limit": null,
                    "dcls_strt_day": "20160920",
                    "dcls_end_day": null,
                    "fin_co_subm_day": "201609201028"
                },
                {
                    "dcls_month": "201609",
                    "fin_co_no": "0010001",
                    "fin_prdt_cd": "WR0001B",
                    "kor_co_nm": "우리은행",
                    "fin_prdt_nm": "우리웰리치100예금(회전형)",
                    "join_way": "영업점,인터넷,스마트폰",
                    "mtrt_int": "만기 후\n- 1개월이내 : 만기시점약정이율×50%",
                    "spcl_cnd": "최고 연 0.2%p 우대이율",
                    "join_deny": "1",
                    "join_member": "실명의 개인",
                    "etc_note": "-가입자가 환갑, 칠순, 팔순, 구순, 백순 사유로 중도해지 시 기본이자율을 중도해지 이자율 적용",
                    "max_limit": null,
                    "dcls_strt_day": "20160920",
                    "dcls_end_day": null,
                    "fin_co_subm_day": "201609201028"
                }
            ]
        }
    }'''

    # JSON 데이터 파싱
    data = json.loads(json_data)

    # 데이터베이스에 데이터 삽입
    for item in data['result']['baseList']:
        financial_product = FinancialProduct(
            fin_co_no=item['fin_co_no'],
            fin_prdt_cd=item['fin_prdt_cd'],
            kor_co_nm=item['kor_co_nm'],
            fin_prdt_nm=item['fin_prdt_nm'],
            prdt_type='D' if item['fin_prdt_cd'].startswith('WR') else 'S',  # 예금/적금 구분
            join_way=item['join_way'],
            mtrt_int=item['mtrt_int'],
            spcl_cnd=item['spcl_cnd'],
            join_deny=True if item['join_deny'] == '1' else False,
            join_member=item['join_member'],
            etc_note=item['etc_note'],
            max_limit=item.get('max_limit', None),
            dcls_strt_day=item['dcls_strt_day'],
            dcls_end_day=item.get('dcls_end_day', None),
            fin_co_subm_day=item['fin_co_subm_day'],
        )
        financial_product.save()

    return render(request, 'insert_complete.html')

from django.shortcuts import render

def survey(request):
    return render(request, 'myapp/survey.html')
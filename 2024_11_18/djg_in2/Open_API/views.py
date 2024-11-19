from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import companyList, companyListOption, IntegrationProduct, IntegrationProductOption
from .serializers import CompanyListSerializer, CompanyListOptionSerializer, IntegrationProductSerializer, IntegrationProductOptionSerializer
import requests
from django.conf import settings
from datetime import datetime

# 데이터베이스에 상품 데이터를 저장하는 함수
def save_product_data(product_data, option_data, product_type):
    # 기존 데이터 삭제 (리셋)
    # IntegrationProduct.objects.all().delete()
    # IntegrationProductOption.objects.all().delete()

    # 상품 데이터를 IntegrationProduct 모델에 저장
    for item in product_data:
        product = IntegrationProduct.objects.create(
            dcls_month=item.get('dcls_month'),
            fin_co_no=item.get('fin_co_no'),
            fin_prdt_cd=item.get('fin_prdt_cd'),
            kor_co_nm=item.get('kor_co_nm'),
            fin_prdt_nm=item.get('fin_prdt_nm'),
            join_way=item.get('join_way'),
            mtrt_int=item.get('mtrt_int'),
            spcl_cnd=item.get('spcl_cnd'),
            join_deny=item.get('join_deny'),
            join_member=item.get('join_member'),
            etc_note=item.get('etc_note'),
            max_limit=item.get('max_limit'),
            loan_inci_expn=item.get('loan_inci_expn'),
            erly_rpay_fee=item.get('erly_rpay_fee'),
            dly_rate=item.get('dly_rate'),
            loan_lmt=item.get('loan_lmt'),
            dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d').date(),
            dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d').date() if item.get('dcls_end_day') else None,
            fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M'),
            type_a = product_type
        )

        # 상품 옵션 데이터를 IntegrationProductOption 모델에 저장
        for option in option_data:
            if option.get('fin_prdt_cd') == item.get('fin_prdt_cd'):
                IntegrationProductOption.objects.create(
                    # 예금/적금 상품에 관련된 필드
                    deposit_product=product,
                    dcls_month=option.get('dcls_month'),
                    fin_co_no=option.get('fin_co_no'),
                    fin_prdt_cd=option.get('fin_prdt_cd'),
                    intr_rate_type=option.get('intr_rate_type'),
                    intr_rate_type_nm=option.get('intr_rate_type_nm'),
                    save_trm=option.get('save_trm'),
                    intr_rate=option.get('intr_rate'),
                    intr_rate2=option.get('intr_rate2'),
                    rsrv_type=option.get('rsrv_type'),
                    rsrv_type_nm=option.get('rsrv_type_nm'),
                    mrtg_type=option.get('mrtg_type'),
                    mrtg_type_nm=option.get('mrtg_type_nm'),
                    rpay_type=option.get('rpay_type'),
                    rpay_type_nm=option.get('rpay_type_nm'),
                    lend_rate_type=option.get('lend_rate_type'),
                    lend_rate_type_nm=option.get('lend_rate_type_nm'),
                    lend_rate_min=option.get('lend_rate_min'),
                    lend_rate_max=option.get('lend_rate_max'),
                    lend_rate_avg=option.get('lend_rate_avg'),
                    )

# 공통 함수: 상품 데이터 가져오기 및 저장
def fetch_and_save_product_data(product_type, topFinGrpNo, page_no=1):
    url_map = {
    'deposit': 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json',
    'saving': 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json',
    'mortgageLoan': 'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json',
    'rentHouseLoan': 'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json',
    'company': 'http://finlife.fss.or.kr/finlifeapi/companySearch.json',
    }

    url = url_map[product_type]
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': topFinGrpNo,
        'pageNo': str(page_no)
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 데이터 저장 처리
        if product_type == 'company':
            # 회사 정보 저장
            companyList.objects.all().delete()
            companyListOption.objects.all().delete()
            for item in base_list:
                serializer = CompanyListSerializer(data=item)
                if serializer.is_valid():
                    company_instance = serializer.save()
                else:
                    return Response(serializer.errors, status=400)

                # companyListOption 저장
                for option in option_list:
                    if option.get('fin_co_no') == item.get('fin_co_no'):
                        option_data = {'deposit_product': company_instance.pk, **option}
                        option_serializer = CompanyListOptionSerializer(data=option_data)
                        if option_serializer.is_valid():
                            option_serializer.save()
                        else:
                            return Response(option_serializer.errors, status=400)

        else:
            # 상품 데이터 저장
            save_product_data(base_list, option_list, product_type)

        return Response(data)

    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=500)

# 기존 데이터 삭제 (리셋)
@api_view(['POST'])
def delete_product_data(request):
    IntegrationProduct.objects.all().delete()
    IntegrationProductOption.objects.all().delete()
    return Response({'데이터 초기화'})

#########################################################################

# 은행정보 저장
@api_view(['GET'])
def company(request):
    return fetch_and_save_product_data('company', '020000', 1)

# 예금 상품 저장
@api_view(['GET'])
def deposit(request):
    return fetch_and_save_product_data('deposit', '020000', 1)

# 적금 상품 저장
@api_view(['GET'])
def saving(request):
    return fetch_and_save_product_data('saving', '020000', 1)

# 대출 상품 저장
@api_view(['GET'])
def mortgageLoan(request):
    return fetch_and_save_product_data('mortgageLoan', '050000', 1)

# 전세자금 대출 상품 저장
@api_view(['GET'])
def rentHouseLoan(request):
    return fetch_and_save_product_data('rentHouseLoan', '050000', 1)

#########################################################################

# 저장된 상품 데이터를 불러오는 함수들


@api_view(['GET'])
def get_combined_company_data(request):
    # companyList 데이터를 가져옴
    companies = companyList.objects.all()
    company_serializer = CompanyListSerializer(companies, many=True)
    
    # companyListOption 데이터를 가져옴
    options = companyListOption.objects.all()
    option_serializer = CompanyListOptionSerializer(options, many=True)
    
    # 두 데이터 결과를 합쳐서 반환
    return Response({
        'companyList': company_serializer.data,
        'companyListOption': option_serializer.data
    })

@api_view(['GET'])
def get_combined_integration_data(request):
    # IntegrationProduct 데이터를 가져옴
    products = IntegrationProduct.objects.all()
    product_serializer = IntegrationProductSerializer(products, many=True)
    
    # IntegrationProductOption 데이터를 가져옴
    options = IntegrationProductOption.objects.all()
    option_serializer = IntegrationProductOptionSerializer(options, many=True)
    
    # 두 데이터 결과를 합쳐서 반환
    return Response({
        'integrationProducts': product_serializer.data,
        'integrationProductOptions': option_serializer.data
    })


#########################################################################

# 데이터베이스에 상품 데이터를 저장하는 함수(오류)
# def save_product_data2(product_data, option_data, product_type):
#     # 기존 데이터 삭제 (리셋)
#     IntegrationProduct.objects.all().delete()
#     IntegrationProductOption.objects.all().delete()

#     # 상품 데이터를 IntegrationProduct 모델에 저장
#     for item in product_data:
#         # IntegrationProduct 직렬화
#         serializer = IntegrationProductSerializer(data=item)
#         if serializer.is_valid():
#             product = serializer.save()  # 유효한 경우 DB에 저장
#         else:
#             return Response(serializer.errors, status=400)

#         # 상품 옵션 데이터를 IntegrationProductOption 모델에 저장
#         for option in option_data:
#             if option.get('fin_prdt_cd') == item.get('fin_prdt_cd'):
#                 option_data = {
#                     'product': product.pk,  # 저장된 IntegrationProduct 객체
#                     **option
#                 }
#                 option_serializer = IntegrationProductOptionSerializer(data=option_data)
#                 if option_serializer.is_valid():
#                     option_serializer.save()
#                 else:
#                     return Response(option_serializer.errors, status=400)



# 테스트용 임시 뷰
from .models import TestItem
from .serializers import TestItemSerializer

@api_view(['GET', 'POST'])
def handle_survey_data(request):
    # GET 요청: 데이터베이스에서 survey 데이터를 가져옴
    if request.method == 'GET':
        # TestItem 데이터 조회
        items = TestItem.objects.all()
        item_serializer = TestItemSerializer(items, many=True)
        return Response({
            'surveyData': item_serializer.data
        })
    
    # POST 요청: 새로운 데이터를 추가
    elif request.method == 'POST':
        serializer = TestItemSerializer(data=request.data)
        if serializer.is_valid():
            # 새로운 survey 데이터 저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_survey_data(request, survey_id):
    print(survey_id)
    try:
        # 주어진 survey_id에 해당하는 데이터 조회
        survey_data = TestItem.objects.get(id=survey_id)
    except TestItem.DoesNotExist:
        return Response({'error': 'Survey data not found'}, status=status.HTTP_404_NOT_FOUND)

    # 요청된 데이터로 serializer 업데이트
    serializer = TestItemSerializer(survey_data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
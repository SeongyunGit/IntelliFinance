from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import companyList, companyListOption, IntegrationProduct, IntegrationProductOption
from .serializers import CompanyListSerializer, CompanyListOptionSerializer, IntegrationProductSerializer, IntegrationProductOptionSerializer
import requests
from django.conf import settings
from datetime import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

# 데이터베이스에 상품 데이터를 저장하는 함수
def save_product_data(product_data, option_data, product_type):
    for item in product_data:
        # 기존 데이터가 존재하는지 확인
        product, created = IntegrationProduct.objects.update_or_create(
            fin_prdt_cd=item.get('fin_prdt_cd'),
            defaults={
                'dcls_month': item.get('dcls_month'),
                'fin_co_no': item.get('fin_co_no'),
                'kor_co_nm': item.get('kor_co_nm'),
                'fin_prdt_nm': item.get('fin_prdt_nm'),
                'join_way': item.get('join_way'),
                'mtrt_int': item.get('mtrt_int'),
                'spcl_cnd': item.get('spcl_cnd'),
                'join_deny': item.get('join_deny'),
                'join_member': item.get('join_member'),
                'etc_note': item.get('etc_note'),
                'max_limit': item.get('max_limit'),
                'loan_inci_expn': item.get('loan_inci_expn'),
                'erly_rpay_fee': item.get('erly_rpay_fee'),
                'dly_rate': item.get('dly_rate'),
                'loan_lmt': item.get('loan_lmt'),
                'dcls_strt_day': item.get('dcls_strt_day'),
                'dcls_end_day': item.get('dcls_end_day'),
                'fin_co_subm_day': item.get('fin_co_subm_day'),
                'type_a': product_type,
            },
        )

        for option in option_data:
            if option.get('fin_prdt_cd') == item.get('fin_prdt_cd'):
                option_instance, option_created = IntegrationProductOption.objects.update_or_create(
                    deposit_product=product,
                    fin_prdt_cd=option.get('fin_prdt_cd'),
                    save_trm=option.get('save_trm'),  # 기본적으로 unique한 조건을 추가해야 함
                    defaults={
                        'dcls_month': option.get('dcls_month'),
                        'fin_co_no': option.get('fin_co_no'),
                        'intr_rate_type': option.get('intr_rate_type'),
                        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                        'intr_rate': option.get('intr_rate'),
                        'intr_rate2': option.get('intr_rate2'),
                        'rsrv_type': option.get('rsrv_type'),
                        'rsrv_type_nm': option.get('rsrv_type_nm'),
                        'mrtg_type': option.get('mrtg_type'),
                        'mrtg_type_nm': option.get('mrtg_type_nm'),
                        'rpay_type': option.get('rpay_type'),
                        'rpay_type_nm': option.get('rpay_type_nm'),
                        'lend_rate_type': option.get('lend_rate_type'),
                        'lend_rate_type_nm': option.get('lend_rate_type_nm'),
                        'lend_rate_min': option.get('lend_rate_min'),
                        'lend_rate_max': option.get('lend_rate_max'),
                        'lend_rate_avg': option.get('lend_rate_avg'),
                    },
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
            # 회사 정보 처리
            for item in base_list:
                # `companyList`에 대한 업데이트 또는 생성
                company_instance, created = companyList.objects.update_or_create(
                    fin_co_no=item.get('fin_co_no'),  # fin_co_no가 기준
                    defaults={  # 업데이트할 데이터
                        'dcls_month': item.get('dcls_month'),
                        'kor_co_nm': item.get('kor_co_nm'),
                        'dcls_chrg_man': item.get('dcls_chrg_man'),
                        'homp_url': item.get('homp_url'),
                        'cal_tel': item.get('cal_tel'),
                    }
                )

                # `companyListOption` 저장
                for option in option_list:
                    if option.get('fin_co_no') == item.get('fin_co_no'):
                        # `fin_co_no`와 `area_cd`를 기준으로 업데이트 또는 생성
                        option_instance, option_created = companyListOption.objects.update_or_create(
                            fin_co_no=option.get('fin_co_no'),  # fin_co_no를 기준으로
                            area_cd=option.get('area_cd'),      # area_cd를 기준으로
                            defaults={  # 옵션 데이터를 업데이트
                                'dcls_month': option.get('dcls_month'),
                                'area_cd': option.get('area_cd'),
                                'area_nm': option.get('area_nm'),
                                'exis_yn': option.get('exis_yn'),
                            }
                        )

        else:
            # 상품 데이터 저장
            save_product_data(base_list, option_list, product_type)

        return Response(data)

    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=500)
    

#########################################################################

from django.contrib.auth.decorators import login_required, user_passes_test

# 관리자만 접근할 수 있도록 제한하는 함수
def is_admin(user):
    return user.is_staff  # is_staff가 True인 경우 관리자 페이지 접근 가능

# 관리자가 아니면 접근을 거부하는 데코레이터 적용
# 기존 데이터 삭제 (리셋)
@api_view(['POST'])
@login_required
@user_passes_test(is_admin)
def delete_product_data(request):
    IntegrationProduct.objects.all().delete()
    IntegrationProductOption.objects.all().delete()
    return Response({'데이터 초기화'})

#########################################################################

# 은행정보 저장
@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def company(request):
    return fetch_and_save_product_data('company', '020000', 1)
    

# 예금 상품 저장
@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def deposit(request):
    return fetch_and_save_product_data('deposit', '020000', 1)
  

# 적금 상품 저장
@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def saving(request):
    return fetch_and_save_product_data('saving', '020000', 1)
    

# 대출 상품 저장
@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
def mortgageLoan(request):
    return fetch_and_save_product_data('mortgageLoan', '050000', 1)
    
# 전세자금 대출 상품 저장
@api_view(['GET'])
@login_required
@user_passes_test(is_admin)
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

#############################################################################

#좋아한 상품
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def toggle_like(request, bank_id):
#     """
#     좋아요 추가/취소
#     """
#     try:
#         print(request.user)
#         bank_product = IntegrationProduct.objects.get(id=bank_id)
#         like, created = Like.objects.get_or_create(user=request.user, bank_product=bank_product)

#         if not created:
#             # 좋아요 이미 존재 -> 삭제
#             like.delete()
#             is_liked = False
#         else:
#             # 새로 생성 -> 좋아요 추가
#             is_liked = True

#         return Response({
#             "is_liked": is_liked,
#         })

#     except IntegrationProduct.DoesNotExist:
#         return Response({"error": "상품을 찾을 수 없습니다."}, status=404)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def liked_products(request):
#     """
#     사용자가 좋아요한 상품 목록
#     """
#     liked_products = IntegrationProduct.objects.filter(liked_by__user=request.user)
#     data = [
#         {
#             "id": product.pk,
#             "name": product.kor_co_nm,
#             "mtrt_int": product.mtrt_int,
#             "type_a": product.type_a,
#         }
#         for product in liked_products
#     ]
#     return Response(data)

#########################################################################

from .models import Comments
from .serializers import CommentSerializer

@api_view(['POST'])
def comments_create(request, diary_pk):
    try:
        # 다이어리 객체가 아니라, IntegrationProduct 객체를 가져옵니다.
        bank_product = IntegrationProduct.objects.get(pk=diary_pk)  
    except IntegrationProduct.DoesNotExist:
        return Response({'message': 'Product not found.'}, status=404)  # 제품이 존재하지 않으면 404 반환

    # 로그인한 사용자 정보 가져오기
    user = request.user
    
    # 요청으로 받은 데이터로 댓글 생성
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():  # 유효한 데이터인지 확인
        # user와 bank_product 연결 후 저장
        serializer.save(user=user, bank_product=bank_product)

        return Response({
            'message': 'Comment created successfully.',
            'comment': serializer.data
        }, status=201)  # 댓글 생성 후 데이터 반환
    return Response({
        'message': 'Invalid data.',
        'errors': serializer.errors
    }, status=400)  # 유효하지 않은 데이터일 경우 오류 메시지 반환

@api_view(['POST'])
def comments_delete(request, comment_pk):
    try:
        # 삭제할 댓글을 가져옵니다.
        comment = Comments.objects.get(pk=comment_pk)
    except Comments.DoesNotExist:
        return Response({'message': 'Comment not found.'}, status=404)  # 댓글이 없으면 404 반환

    # 댓글 삭제
    comment.delete()

    return Response({
        'message': 'Comment deleted successfully.',
    }, status=200)  # 댓글 삭제 성공 메시지 반환

#########################################################################




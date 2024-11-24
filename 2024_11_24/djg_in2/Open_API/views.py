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
from .models import Like

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, bank_id):
    """
    좋아요 추가/취소
    """
    if request.method == 'POST':
            product = IntegrationProduct.objects.get(pk=bank_id)
            if request.user != product.like_users:
                # 좋아요를 누른 유저가 이미 좋아요를 눌렀으면 취소
                if request.user in product.like_users.all():
                    product.like_users.remove(request.user)
                else:
                    # 좋아요를 누르지 않았으면 추가
                    product.like_users.add(request.user)
                    
                # 로그인한 유저가 좋아요한 모든 게시글 가져오기
                liked_articles = IntegrationProduct.objects.filter(like_users=request.user)

                # 좋아요한 게시글들의 정보를 반환
                liked_article_data = liked_articles.values('id',)
                

                # 좋아요가 변경된 후 좋아요한 모든 게시글 정보 응답
                return Response({
                    'liked_articles': list(liked_article_data),
                    'message': 'Successfully toggled like status'
                }, status=status.HTTP_200_OK)
            
    return Response({'detail': 'Invalid method or user'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liked_products(request):
    """
    사용자가 좋아요한 상품 목록
    """
    liked_products = IntegrationProduct.objects.filter(like_users=request.user)
    data = [
        {
            "id": product.pk,
            "name": product.kor_co_nm,
            "mtrt_int": product.mtrt_int,
            "type_a": product.type_a,
        }
        for product in liked_products
    ]
    return Response(data)

#########################################################################

from .models import Comments
from .serializers import CommentSerializer

# GET 요청: 모든 댓글 조회
@api_view(['GET'])
def comments_get(request):
    # 모든 댓글 가져오기
    comments = Comments.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response({
        'message': 'Comments retrieved successfully.',
        'comments': serializer.data
    }, status=200)


# POST 요청: 댓글 작성
@api_view(['POST'])
def comments_create(request, product_pk):
    try:
        # IntegrationProduct 객체 가져오기
        bank_product = IntegrationProduct.objects.get(pk=product_pk)
    except IntegrationProduct.DoesNotExist:
        return Response({'message': 'Product not found.'}, status=404)

    # 로그인한 사용자 정보 가져오기
    user = request.user
    
    # 요청으로 받은 데이터로 댓글 생성
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        # user와 bank_product 연결 후 저장
        serializer.save(user=user, bank_product=bank_product)

        # 댓글 생성 후 모든 댓글 반환
        comments = Comments.objects.all()
        all_comments_serializer = CommentSerializer(comments, many=True)
        return Response({
            'message': 'Comment created successfully.',
            'comments': all_comments_serializer.data
        }, status=201)

    return Response({
        'message': 'Invalid data.',
        'errors': serializer.errors
    }, status=400)


# 댓글 삭제
@api_view(['POST'])
def comments_delete(request, comment_pk):
    try:
        # 삭제할 댓글을 가져옵니다.
        comment = Comments.objects.get(pk=comment_pk)
    except Comments.DoesNotExist:
        return Response({'message': 'Comment not found.'}, status=404)  # 댓글이 없으면 404 반환

    # 요청한 유저와 댓글 작성자가 다른 경우
    if comment.user != request.user:
        return Response({'message': 'Permission denied. You can only delete your own comments.'}, status=403)
    
    # 댓글 삭제
    comment.delete()

    # 댓글 삭제 후 모든 댓글 반환
    comments = Comments.objects.all()
    all_comments_serializer = CommentSerializer(comments, many=True)
    return Response({
        'message': 'Comment created successfully.',
        'comments': all_comments_serializer.data
    }, status=201)


#########################################################################
#장고 어드민


#######################################################################
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



from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message": "회원가입이 완료되었습니다.",
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login(request, user)
        return Response({
            "message": "로그인 성공",
            "user": UserSerializer(user).data
        })
    else:
        return Response({
            "message": "이메일 또는 비밀번호가 잘못되었습니다."
        }, status=status.HTTP_400_BAD_REQUEST)

###########################################################################

from .models import Survey
from .serializers import SurveySerializer

@api_view(['GET', 'POST'])
def handle_survey_data(request):
    # GET 요청: 데이터베이스에서 survey 데이터를 가져옴
    if request.method == 'GET':
        # TestItem 데이터 조회
        items = Survey.objects.all()
        item_serializer = SurveySerializer(items, many=True)
        return Response({
            'surveyData': item_serializer.data
        })
    
    # POST 요청: 새로운 데이터를 추가
    elif request.method == 'POST':
        # 요청 데이터에서 user_id, type 가져오기
        user_id = request.data.get('user')
        type_a = request.data.get('type_a')
        
        # Survey 모델의 나머지 필드들은 null로 초기화
        survey_data = {
            'user': user_id,
            'type_a': type_a,
            # 'today' # auto_now=True
            'fin_co_no': None,
            'kor_co_nm': None,
            'intr_rate_type': None,
            'intr_rate_type_nm': None,
            'save_trm': None,
            'intr_rate': None,
            'intr_rate2': None,
            'rsrv_type': None,
            'rsrv_type_nm': None,
            'rpay_type': None,
            'rpay_type_nm': None,
            'lend_rate_type': None,
            'lend_rate_type_nm': None,
            'lend_rate_min': None,
            'lend_rate_max': None,
            'lend_rate_avg': None,
            'mrtg_type': None,
            'mrtg_type_nm': None
        }
        serializer = SurveySerializer(data=survey_data)
        if serializer.is_valid():
            # 새로운 survey 데이터 저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_survey_data(request, survey_id):
    try:
        # 주어진 survey_id에 해당하는 데이터 조회
        survey_data = Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return Response({'error': 'Survey data not found'}, status=status.HTTP_404_NOT_FOUND)

    # 요청된 데이터로 serializer 업데이트
    serializer = SurveySerializer(survey_data, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

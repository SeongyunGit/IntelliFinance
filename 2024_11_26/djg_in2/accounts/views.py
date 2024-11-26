from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import (UserSerializer, 
                          AnnouncementSerializer, SurveySerializer)
from .models import Survey, Announcement


###################################################################################################

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


# 로그인 커스텀(유저pk를 받기위해서)
@api_view(['POST'])
def custom_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # 사용자 인증
    user = authenticate(username=username, password=password)

    if user:
        # 토큰 생성 또는 가져오기
        token, created = Token.objects.get_or_create(user=user)

        # 로그인 성공 시 응답에 user_pk 추가
        return Response({
            'key': token.key,
            'user_pk': user.pk,  # 로그인한 유저의 pk 반환
            'username': user.username,
            'is_staff': user.is_staff  # 관리자 여부 추가
        }, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


#######################################################################################################


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def survey(request, user_id, type):
    # GET 요청: 데이터베이스에서 survey 데이터를 가져옴
    if request.method == 'GET':
        try:
            # 주어진 survey_id에 해당하는 데이터 조회
            survey_data = Survey.objects.get(user=user_id, type_a=type)
        except Survey.DoesNotExist:
            return Response(0)
        
        item_serializer = SurveySerializer(survey_data)
        return Response({'surveyData': item_serializer.data})


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


#######################################################################################################

# 설문 데이터가 없으면 만들기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_survey(request):
    survey_data = request.data  # 'survey_data'가 전달된 데이터
    if not survey_data:
        return Response({"error": "Survey data is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    # survey_data를 사용하여 필요한 로직 처리
    # 예: 새로운 설문 데이터 저장하기
    serializer = SurveySerializer(data=survey_data)
    if serializer.is_valid():
        serializer.save(user=request.user)  # 예: user를 추가하여 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


###################################################################################################

# announcement(공지) 반환
@api_view(['GET'])
def get_announcement(request):
    announcements = Announcement.objects.all()
    announcement_seializer = AnnouncementSerializer(announcements, many=True)

    return Response(announcement_seializer.data)


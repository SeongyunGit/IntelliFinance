from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # 커스터마이즈된 로그인 뷰 연결
    path('login/', views.custom_login, name='account_login'),  

    # 설문 생성 수정 요청
    path('survey/<int:user_id>/<str:type>/', views.survey, name='survey'),
    path('survey/<int:survey_id>/', views.update_survey_data, name='update_survey_data'),
    path('survey/start/', views.start_survey),

    # 공지데이터 요청
    path('announcement/', views.get_announcement, name='get_announcement'),
]
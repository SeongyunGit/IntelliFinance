from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),

    # GET 및 POST 요청을 처리하는 뷰  # 전체 survey 데이터를 처리하는 URL
    path('survey/', views.handle_survey_data, name='handle_survey_data'),
    # PUT 요청만 처리하는 뷰 (특정 survey_id로 수정)  # survey id로 특정 데이터 수정
    path('survey/<int:survey_id>/', views.update_survey_data, name='update_survey_data'),
]
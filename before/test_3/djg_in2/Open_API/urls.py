from django.urls import path
from . import views


urlpatterns = [
    path('company/', views.company),
    path('deposit/', views.deposit),
    path('saving/', views.saving),
    # path('annuitySaving/', views.annuitySaving),
    path('mortgageLoan/', views.mortgageLoan),
    path('rentHouseLoan/', views.rentHouseLoan),
    # path('creditLoan/', views.creditLoan),
    path('get_combined_company_data/', views.get_combined_company_data),
    path('get_combined_integration_data/', views.get_combined_integration_data),
    path('delete_product_data/', views.delete_product_data),

    # # 테스트용 url
    # # GET 및 POST 요청을 처리하는 뷰  # 전체 survey 데이터를 처리하는 URL
    # path('survey/', views.handle_survey_data, name='handle_survey_data'),
    # # PUT 요청만 처리하는 뷰 (특정 survey_id로 수정)  # survey id로 특정 데이터 수정
    # path('survey/<int:survey_id>/', views.update_survey_data, name='update_survey_data'),
]

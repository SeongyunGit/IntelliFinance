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
    # path('create_item/', views.create_item, name='create_item'),
]

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
    
    path('api/bank/<int:bank_id>/like/', views.toggle_like, name='toggle_like'),
    path('api/bank/liked/', views.liked_products, name='liked_products'),
]

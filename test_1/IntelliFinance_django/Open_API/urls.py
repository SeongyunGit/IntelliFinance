from django.urls import path
from . import views


urlpatterns = [
    path('company/', views.company),
    path('Deposit/', views.Deposit),
    path('saving/', views.saving),
    path('annuitySaving/', views.annuitySaving),
    path('mortgageLoan/', views.mortgageLoan),
    path('rentHouseLoan/', views.rentHouseLoan),
    path('creditLoan/', views.creditLoan),
]

from django.urls import path
from . import views


urlpatterns = [
    # 환율 정보
    path('exchangedata/', views.fetch_and_save_exchange_rates, name='fetch_and_save_exchange_rates'),
]

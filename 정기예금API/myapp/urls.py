from django.urls import path
from . import views

urlpatterns = [
    path('fetch_and_store_deposit_products/', views.fetch_and_store_deposit_products, name='fetch_and_store_deposit_products'),
]

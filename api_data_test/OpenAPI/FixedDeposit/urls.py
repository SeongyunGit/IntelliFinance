from django.urls import path
from . import views

urlpatterns = [
    path('', views.FixedDeposit, name='FixedDeposit'),
]

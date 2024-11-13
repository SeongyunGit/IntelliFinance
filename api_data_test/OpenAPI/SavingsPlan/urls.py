from django.urls import path
from . import views

urlpatterns = [
    path('', views.SavingsPlan, name='SavingsPlan'),
]

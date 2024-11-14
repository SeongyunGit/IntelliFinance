from django.urls import path
from .views import SurveyResultView
from . import views

app_name='intellifiarce_back'

urlpatterns = [
    path('survey/', views.survey, name='survey'),
]
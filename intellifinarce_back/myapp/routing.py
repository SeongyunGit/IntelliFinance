from django.urls import path
from .consumers import SurveyResultConsumer

websocket_urlpatterns = [
    path('ws/survey-results/<int:question_id>/', SurveyResultConsumer.as_asgi()),
]
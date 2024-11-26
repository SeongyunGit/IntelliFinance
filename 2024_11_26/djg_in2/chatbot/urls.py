from django.urls import path
from . import views

urlpatterns = [
    path('api/chat/', views.chat_with_gpt, name='chat_with_gpt'),
    path('api/chat/sort/', views.chat_sort, name='chat_sort'),
]
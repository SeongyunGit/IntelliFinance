from django.urls import path
from . import views
from .views import AnnouncementListCreateView, AnnouncementDetailView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),

    path('announcements/',AnnouncementListCreateView.as_view(), name="announcements"),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name="announcement-detail" )
]
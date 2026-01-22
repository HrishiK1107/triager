from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('submit/', views.submit_report, name='submit'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('home/', views.homepage, name='home'),
    path('report/<int:report_id>/', views.bug_detail, name='bug_detail'),
]

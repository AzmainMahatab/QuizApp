from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-home', views.user_home, name='user_home'),
    path('play/', views.play, name='play'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('submission-result/<int:attempted_question_pk>/', views.submission_result, name='submission_result'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]

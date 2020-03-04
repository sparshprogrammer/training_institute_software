from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about,  name='about'),
    path('login/', views.user_login,  name='login'),
    path('register/', views.registration,  name='register'),
    path('logout/', views.user_logout,  name='logout'),
    path('confirm-account/<str:confirmation_key>/', views.account_confirmation, name='email_confirmation'),

]
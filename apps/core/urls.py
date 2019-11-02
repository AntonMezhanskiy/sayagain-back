from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('user/register/', views.RegisterView.as_view(), name='register'),
    path('user/authenticate/', views.LoginView.as_view(), name='login'),
    path('user/logout/', views.LogoutView.as_view(), name='logout'),
]

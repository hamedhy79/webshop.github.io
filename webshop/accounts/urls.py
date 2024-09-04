from . import views
from django.urls import path
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.UserRegisterView.as_view(), name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

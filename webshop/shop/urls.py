from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name ='shop'

urlpatterns = [
    path('', views.ShopView, name='home'),
    path('checkout/', views.CheckoutView, name='checkout'),
    path('store/', views.StoreView, name='store'),
    path('product/<int:pk>/', views.ProductView, name='product'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('to-bank/<int:order_id>/', views.to_bank, name='to_bank'),
    path('callback/', views.callback, name='callback'),
]

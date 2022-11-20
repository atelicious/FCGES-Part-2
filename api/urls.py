from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from . import views as api_views

urlpatterns = [
    path('stocks/', api_views.get_all_stock, name='get_all_stock'),
    path('customer/', api_views.get_customer_portfolio, name='get_customer_portfolio'),
    path('customer/<str:id>', api_views.get_customer_specific_stock, name='get_customer_specific_stock'),
    path('order/', api_views.process_order, name='process_order'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]
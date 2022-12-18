from django.urls import path, include
from .views import HomePageView, ProfilePageView, LoginPageView
from .views import ProductDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]
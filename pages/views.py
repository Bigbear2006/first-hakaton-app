from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class HomePageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'all_products'

class ProfilePageView(TemplateView):
    template_name = 'profile2.html'

class LoginPageView(TemplateView):
    template_name = 'authorization.html'

# def HomePageView(requests):
#     return HttpResponse('GStore Home Page')
# Create your views here.

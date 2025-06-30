from django.urls import path

# from root.views import home, currency
from . import views

app_name = 'root'

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('currency/', views.currency, name='currency'),
    path('currency/<int:currency_id>/', views.currency_rates, name='currency_rates'),
    # path('category/<int:category_id>/', products, name='category'),
    # path('page/<int:page_number>/', products, name='paginator'),
    # path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    # path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
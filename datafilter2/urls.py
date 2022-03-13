"""datafilter2 URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from datafilter2.api import views

router = routers.DefaultRouter()
router.register(r'datafilter2/products', views.ProductsViewSet, 'products') # function view

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('datafilter2/get_product_by_id/<pk>', views.get_product_by_id), # access product data by id
    # access products by sort_by = attributeName & order_by = ASC or DESC
    # filter_by='category=abc' or filter_by='subcategory=abc'
    path('datafilter2/get_products', views.get_products_sorted), 
]
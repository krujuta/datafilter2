from datafilter2.api.serialization import ProductSerializer
from rest_framework import viewsets
from datafilter2.api.models import Product
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework.response import Response
from rest_framework import status
import logging
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# Create your views here.

# View for products list

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer
    

# get product by id 
@api_view(['GET'])
def get_product_by_id(request,pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        product_serializer = ProductSerializer(product) 
        return JsonResponse(product_serializer.data) 

#get product by order
@api_view(['GET'])
def get_products_sorted(request):
    order_by = request.GET.get('order_by')
    sort_by = request.GET.get('sort_by')

    if((order_by != "") & (order_by == 'DESC')):
        sort_by = '-'+sort_by
    try:
        products = Product.objects.all().order_by(sort_by)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        product_serializer = ProductSerializer(products, many=True) 
        return JsonResponse(product_serializer.data, safe=False) 

# class product_list(viewsets.ModelViewSet):
#     category_slug = None
#     subcategory_slug = None
#     category = None
#     categories = Category.objects.all()
#     subcategory = None
#     # subcategories = Subcategory.objects.all()
#     products = Product.objects.all().order_by('name') #Product.objects.filter(available=True)

#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         # subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
#         products = products.filter(category=category)

#     serializer_class = ProductSerializer

#     # return render(request,
#     #               'selcorshop/product/list.html',
#     #               {'category': category,
#     #                'categories': categories,
#     #                'subcategory': subcategory,
#     #                'subcategories': subcategories,
#     #                'products': products})

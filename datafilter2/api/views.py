from datafilter2.api.serialization import ProductSerializer, CategorySerializer,SubCategorySerializer
from rest_framework import viewsets
from datafilter2.api.models import Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.core import serializers

from .models import Category, Product, SubCategory
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from django.db.models import Q

# Create your views here.

# Products function view
class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
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

#get products by sort_by and order_by
@api_view(['GET'])
def get_products_sorted(request):
    order_by = request.query_params.get('order_by')
    sort_by = request.query_params.get('sort_by')
    filter_by = request.query_params.get('filter_by')

    try:
        products = Product.objects.all().order_by('name') # to get dataset by default

        if not products:
            return Response("Data does not exists in DB",status=status.HTTP_404_NOT_FOUND)  

        else:
            if (sort_by is not None) :
                if((order_by is not None) & (order_by == 'DESC')): 
                    # if order_by is mentioned and DESC, 
                    # add - infront of the attribute name 
                    # to get orders in descenging order
                    # else pass sort_by value as it is for ASC order
                    sort_by = '-'+sort_by 
                products = products.order_by(sort_by) # to get dataset as sort_by param   

            elif((filter_by is not None)):
                filter_by = filter_by.replace('\'',"") # for removing additional characters
                filter_by_value = filter_by.split('=',1)[1] # to get filter_by value
                if('_category' not in filter_by): 
                    # we are checking if _category word is not there in the param, 
                    # it means category filter is applied
                    products = products.filter(Q(category__name=filter_by_value))
                else:
                    products = products.filter(Q(subcategory__name=filter_by_value))
            else:                   
                products = products

    except Product.DoesNotExist:
        # if products not found
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        # more methods can be added for the same view. hence, 
        # the method GET is mentioned to return the appropriate result
        product_serializer = ProductSerializer(products, many=True) 
        return JsonResponse(product_serializer.data, safe=False) 

# Category function view - not used in this application, used for testing
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer   

# Category function view - not used in this application, used for testing
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().order_by('name')
    serializer_class = SubCategorySerializer
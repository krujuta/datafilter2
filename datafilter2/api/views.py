from datafilter2.api.serialization import ProductSerializer
from rest_framework import viewsets
from datafilter2.api.models import Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse

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

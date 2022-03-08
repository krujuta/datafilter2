from django.shortcuts import render
from datafilter2.api.serialization import ProductSerializer
from rest_framework import viewsets
from datafilter2.api.models import Product

# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-date_joined')
    serializer_class = ProductSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

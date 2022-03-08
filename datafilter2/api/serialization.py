from rest_framework import serializers
from .models import Product

# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = ['sub_category']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url','name', 'price', 'vendor', 'category', 'product_description', 'image']
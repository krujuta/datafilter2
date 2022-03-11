from rest_framework import serializers
from .models import Product, Category, SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('name')

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ('name','subcategories')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True) 
    class Meta:
        model = Product
        fields = ('name', 'price', 'vendor', 
        'product_description', 'image','admissibleregion','categories')

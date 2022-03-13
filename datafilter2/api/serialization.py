from rest_framework import serializers
from .models import Product, Category, SubCategory

#for serializing sub-category data
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']

#for serializing category data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

#for serializing product data
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #for serializing nested data
    subcategory = SubCategorySerializer() 
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['name', 'price', 'vendor', 'product_description',
         'image','admissibleregion','category','subcategory']
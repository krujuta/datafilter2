from tkinter import CASCADE
from django.db import models

# Create your models here.

# Class model for category
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

# Class model for sub-category
class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    # foreign key /  one-to-one mapping 
    # with assumption that, every sub-category will be a part of single category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Class model for product
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    product_description = models.TextField(blank=True)
    price = models.IntegerField()
    vendor = models.TextField(default=False)
    admissibleregion = (
        ('EU', 'EU'),
        ('US', 'US'),
        ('CHINA', 'CHINA'),
        ('ROW', 'ROW'),
    )
    # one to one field mapping with the assumption 
    # that every product will have a single sub-category and category
    subcategory = models.OneToOneField(SubCategory, blank=False, on_delete=models.CASCADE) 
    category = models.OneToOneField(Category, blank=False, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(blank=False)
    price = models.BigIntegerField(blank=False)
    vendor = models.TextField(blank=False)
    category = models.CharField(max_length=32, blank=True, null=True)
    product_description = models.CharField(max_length=255,blank=False)
    image = models.TextField(blank=False) #placeholder for images
    admissible_region = (
        ('EU', 'EU'),
        ('US', 'US'),
        ('CHINA', 'CHINA'),
        ('ROW', 'ROW'),
    )

    def __str__(self): # test for checking product model
        return self.name

# class SubCategory(models.Model):
#     sub_category = models.CharField(max_length=32, blank=True, null=True)
#     category_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sub_category')
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.OneToOneField(Category, blank=False, primary_key=True, on_delete=models.CASCADE)
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
    subcategory = models.OneToOneField(SubCategory, blank=False, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, blank=False, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
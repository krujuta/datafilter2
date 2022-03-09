from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.

# Class model for product
class Product(models.Model):
    # category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
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

#     slug = AutoSlugField(unique = True, populate_from=('name',))
#     def __str__(self):
#         return self.title

#     def get_cat_list(self):
#         k = self.category # for now ignore this instance method
        
#         breadcrumb = ["dummy"]
#         while k is not None:
#             breadcrumb.append(k.slug)
#             k = k.parent
#         for i in range(len(breadcrumb)-1):
#             breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
#         return breadcrumb[-1:0:-1]

# # Class model for category
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     slug = AutoSlugField(unique = True, populate_from=('name',))
#     parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)

#     class Meta:
#         #enforcing that there can not be two categories under a parent with same slug
#         # __str__ method elaborated later in post.  use __unicode__ in place of
#         # __str__ if you are using python 2
#         unique_together = ('slug', 'parent',)    
#         verbose_name_plural = "categories"     

#     def __str__(self):                           
#         full_path = [self.name]                  
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#         return ' -> '.join(full_path[::-1])
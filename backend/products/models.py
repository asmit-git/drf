from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2, default=99.99)


    '''
    let's add the property of saleprice to check the actual usage of serializers in django rest framework.
    this new field property cannot be accessed from model_to_dict which can be done by drf serializers with ease.
    '''

    @property 
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return "100"
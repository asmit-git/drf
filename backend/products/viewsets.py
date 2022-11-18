from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list all 
    get -> get detail
    post - > post data
    put -> update
    patch -> partial update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
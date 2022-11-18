from rest_framework import mixins, viewsets
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


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list all 
    get -> retrieve detail
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

'''
product_list_create_view = ProductListCreateAPIView.as_view() similar as in views
'''
product_list_view = ProductGenericViewSet.as_view({'get':'list'})

product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})

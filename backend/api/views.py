# import json
from django.forms.models import model_to_dict # for changing django model to Python Dict

# from django.http import JsonResponse # To return Text/HTML data type we can use HttpResponse
'''
Django rest framework implementation
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response #this response is going to replace the JsonResponse 

# def api_home(request,*args,**kwargs):
#     # request - > HttpRequest -> Django
#     # print(dir(request))
#     # request.body
#     print(request.GET) ## Returns url query params
#     print(request.POST)
#     body = request.body #byte string of JSON data
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data.keys)
#     #data['headers'] = request.headers
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type

#     return JsonResponse(data)

from products.models import Product
from products.serializers import ProductSerializer

# def api_home(requests,*args,**kwargs):
#     model_data =  Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         '''
#         We will be changing the model instance into a Python Dict and return josn to the client
#         '''
#         data = model_to_dict(model_data, fields=['id','title'])        
#     return JsonResponse(data)

# @api_view(["GET"])
# def api_home(requests,*args,**kwargs):
#     # model_data =  Product.objects.all().order_by("?").first()
#     '''
#     DRF API View
#     '''
#     instance =  Product.objects.all().order_by("?").first()
#     data = {}
#     # if model_data:
#     #     data = model_to_dict(model_data, fields=['id','title','price','sale_price'])  # the sale_price won't be rendered that's why we will use drf searializers4

#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)


@api_view(["POST"])
def api_home(requests,*args,**kwargs):
    # model_data =  Product.objects.all().order_by("?").first()
    '''
    DRF API View
    '''
    serializer = ProductSerializer(data=requests.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    # return Response({"invalid":"not good data"})
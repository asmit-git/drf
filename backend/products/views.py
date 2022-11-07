from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication

from .models import Product
from .premissions import IsStaffEditorPermission
from .serializers import ProductSerializer

'''
Generic Views
'''
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    '''
    changing default settings in cfehome>>settings.py for authentication classes we can now have permissions only and authetication
    classes will be applied by default
    '''
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication] #TokenAuthentication with changed keyword from api>>authentication.py
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [IsStaffEditorPermission]

    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    # lookup_field = 'pk' ??

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions]  # first off register the model in admin.py and model permissions for user are set from admin dashboard
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()
    

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_destroy(self,instance):
        #anything to do with the instance
       super().perform_destroy(instance)
            
product_delete_view = ProductDestroyAPIView.as_view()
    

# class ProductListAPIView(generics.ListAPIView):
#     '''
#     we can do the list action all in all in a create section ProductCreateAPIView -> ProductListCreateAPIView
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()

'''
Core class based views -> Genereic Views breakdown
Mixins and Generic API View
In case of function based view we wrote conditions however in class based view we write function
eg: if(request=="GET") ~equivalent~ def get(self,request,*args,**kwargs):
'''

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    #Create model mixins
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is done from mixins"
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()

'''
Function based views
one single function based view combining all the views
'''
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            #detail view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404
            #return Response()
            
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)

        # url args ??
        # get request -> detail view
        # list view 
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            # instance = form.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)



from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk>/',views.ProductDetailAPIView.as_view())
    path('',views.product_list_create_view),
    path('<int:pk>/update/',views.product_update_view),
    path('<int:pk>/delete/',views.product_delete_view),
    path('<int:pk>/',views.product_detail_view),

    # Implementing Class based Mixins View
    # path('',views.product_mixin_view),
    # path('<int:pk>/',views.product_mixin_view),

    # Implementing function based view urls
    # path('',views.product_alt_view),
    # path('<int:pk>/',views.product_alt_view)
]
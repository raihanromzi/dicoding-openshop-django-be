# router = SimpleRouter()
# router.register(r'products', ProductViewSet, basename='products')
#
# urlpatterns = router.urls
from django.urls import path

from open_shop import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<uuid:pk>/', views.ProductDetail.as_view(),
         name='product-detail'),

]

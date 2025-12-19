from rest_framework.viewsets import ModelViewSet

from open_shop.models import Product
from open_shop.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

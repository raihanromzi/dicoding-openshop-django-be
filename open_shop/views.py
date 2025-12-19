from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from open_shop.models import Product
from open_shop.serializers import ProductSerializer


class ProductList(APIView):
    def post(self, request):
        product = ProductSerializer(data=request.data,
                                    context={'request': request})

        if product.is_valid(raise_exception=True):
            product.save()
            return Response(data=product.data, status=status.HTTP_201_CREATED)

        return Response(data=product.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Product.objects.filter(is_delete=False)

        name = request.query_params.get('name')
        if name is not None:
            products = products.filter(name=name)

        location = request.query_params.get('location')
        if location is not None:
            products = products.filter(location=location)

        return Response({"products": ProductSerializer(products, many=True,
                                                       context={
                                                           'request': request}).data},
                        status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound('Not found.')

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product,
                                       context={'request': request})
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product, data=request.data,
                                       context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.is_delete = True
        product.save(update_fields=['is_delete'])
        return Response(status=status.HTTP_204_NO_CONTENT)

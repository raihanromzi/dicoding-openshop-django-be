from rest_framework import serializers
from rest_framework.reverse import reverse

from open_shop.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'shop', 'price', 'sku', 'description',
                  'location', 'discount', 'category', 'stock', 'is_available',
                  'picture', 'is_delete', '_links']

    def validate_value(self, value, field):
        if value < 0:
            raise serializers.ValidationError(
                f'{field} must be greater than zero.')
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Price must be greater than zero.')
        return value

    def validate_discount(self, value):
        return self.validate_value(value, 'Discount')

    def validate_stock(self, value):
        return self.validate_value(value, 'Stock')

    def get__links(self, obj):
        request = self.context.get('request')

        list_url = reverse('product-list', request=request)
        detail_url = reverse('product-detail', kwargs={'pk': obj.pk},
                             request=request)

        return [
            {
                "rel": "self",
                "href": list_url,
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "PUT",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": detail_url,
                "action": "DELETE",
                "types": ["application/json"]
            }
        ]

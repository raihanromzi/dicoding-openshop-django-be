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

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must be zero or greater.")
        return value

    def get__links(self, obj):
        request = self.context.get('request')

        list_url = reverse('', request=request)
        detail_url = reverse('', kwargs={'pk': obj.pk},
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

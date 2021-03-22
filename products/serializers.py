from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSizeSerializer(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['id','title','active']


from rest_framework.viewsets import ModelViewSet
from products.models import ProductSize, Product
from products.serializers import (
 ProductSizeSerializer,
    ProductSerializer
)
from rest_framework.permissions import IsAuthenticated


class ProductSizeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.prefetch_related(
                'available_sizes').all()
    serializer_class = ProductSerializer
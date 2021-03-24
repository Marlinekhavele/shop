from rest_framework.viewsets import ModelViewSet
from products.models import ProductSize, Product
from products.serializers import (
 ProductSizeSerializer,
    ProductSerializer
)
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class ProductSizeViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,IsAuthenticatedOrReadOnly]

    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,IsAuthenticatedOrReadOnly]
    queryset = Product.objects.prefetch_related(
                'available_sizes').all()
    serializer_class = ProductSerializer
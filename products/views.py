from rest_framework.viewsets import ModelViewSet
from products.models import ProductSize, Product
from products.serializers import (
 ProductSizeSerializer,
    ProductSerializer
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductSizeViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.prefetch_related(
                'available_sizes').all()
    serializer_class = ProductSerializer
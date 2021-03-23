from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from products.models import  Product
from products.serializers import (
    
    ProductSerializer
)

class ProductViewSet(ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
    )
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(customer)
        return Response(serializer.data)

    def create(self, request):
        new_product = ProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            return Response(new_product.data, status=201)
        return Response(new_product.errors, status=400)
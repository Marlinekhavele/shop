from rest_framework import routers

from products.views import (
    ProductViewSet,ProductSizeViewSet
)

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'sizes', ProductSizeViewSet,basename='sizes')

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter
from .views import ExchangeViewSet

router = DefaultRouter()
router.register(r'', ExchangeViewSet, basename='Exchanges')
exchange_urls = router.urls
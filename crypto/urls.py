from rest_framework.routers import DefaultRouter
from .views import CryptosViewSet


router = DefaultRouter()
router.register(r'', CryptosViewSet, basename='Criptomoedas')
cryptos_urls = router.urls
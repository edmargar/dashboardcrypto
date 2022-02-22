from rest_framework.routers import DefaultRouter
from .views import CMCViewSet


router = DefaultRouter()
router.register(r'', CMCViewSet, basename='cmc'),
cmc_urls = router.urls

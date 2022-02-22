from rest_framework.routers import DefaultRouter
from .views import NegotiationViewSet

router = DefaultRouter()
router.register(r'', NegotiationViewSet, basename='Negociações')
negotiation_urls = router.urls
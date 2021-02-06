from rest_framework import routers
from .views import TopCastleViewSet, NationalTreasureViewSet, ExistenceViewSet

router = routers.DefaultRouter()
router.register(r'top100', TopCastleViewSet)
router.register(r'national-treasure', NationalTreasureViewSet)
router.register(r'existence', ExistenceViewSet)

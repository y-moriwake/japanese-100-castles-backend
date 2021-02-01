from rest_framework import routers
from .views import CastleViewSet

router = routers.DefaultRouter()
router.register(r'castles', CastleViewSet)

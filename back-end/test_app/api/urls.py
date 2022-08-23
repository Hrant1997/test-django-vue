from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shipments', views.ShipmentViewSet, basename='shipment')
urlpatterns = router.urls
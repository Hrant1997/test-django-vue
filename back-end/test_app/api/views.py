from .models import Shipment
from .serializers import ShipmentSerializer
from rest_framework import viewsets
  
class ShipmentViewSet(viewsets.ModelViewSet):

    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

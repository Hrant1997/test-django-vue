from rest_framework import serializers
from .models import Shipment
  
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'shipping_address', 'biling_address', 'product_price', 'delivery_cost', 'final_price')

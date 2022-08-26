from django.db import models

class Shipment(models.Model):
    shipping_address = models.CharField(max_length=255)
    biling_address = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits = 8, decimal_places = 2)
    delivery_cost = models.DecimalField(max_digits = 8, decimal_places = 2)
    final_price = models.DecimalField(max_digits = 8, decimal_places = 2)

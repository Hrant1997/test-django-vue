from decimal import Decimal
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

from .models import Shipment
class ShipmentTests(APITestCase, URLPatternsTestCase):
    fixtures = ['tests.json', ]
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_create_shipment(self):
        url = reverse('shipment-list')
        create_data = {
            'biling_address': 'test address',
            'delivery_cost': 10,
            'product_price': 50,
            'final_price': 60
        }
        response = self.client.post(url, create_data)
        res_data = response.json()
        self.assertEqual(res_data['shipping_address'], ['This field is required.'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        create_data['shipping_address'] = 'Yerevan'
        response = self.client.post(url, format='json', data=create_data)
        res_data = response.json()
        self.assertTrue(isinstance(res_data['id'], int))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        shipment = Shipment.objects.get(pk=res_data['id'])
        self.assertEqualShipment(shipment, res_data)

    def test_list_shipment(self):
        url = reverse('shipment-list')
        response = self.client.get(url, format='json')
        res_data = response.json()

        shipments = Shipment.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_data), shipments.count())

        for index, shipment in  enumerate(shipments):
            self.assertEqualShipment(shipment, res_data[index])

    def test_retrieve_shipment(self):
        shipment = Shipment.objects.first()
        url = reverse('shipment-detail', kwargs={'pk': shipment.id })
        response = self.client.get(url, format='json')
        res_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqualShipment(shipment, res_data)
        
    def test_upadate_shipment(self):
        shipment = Shipment.objects.first()
        url = reverse('shipment-detail', kwargs={'pk': shipment.id })
        update_data = {
            'biling_address': 'test address',
            'delivery_cost': 10,
            'product_price': 50,
            'final_price': 60
        }
        response = self.client.put(url, format='json', data=update_data)
        res_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res_data['shipping_address'], ['This field is required.'])

        update_data['shipping_address'] = 'Yerevan'
        response = self.client.put(url, format='json', data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = response.json()
        shipment = Shipment.objects.get(pk=shipment.id)
        self.assertEqualShipment(shipment, res_data)

    def test_delete_shipment(self):
        shipment = Shipment.objects.first()
        url = reverse('shipment-detail', kwargs={'pk': shipment.id })
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            shipment = Shipment.objects.get(pk=shipment.id)
        except Shipment.DoesNotExist as err:
            self.assertEqual(err.__str__(), 'Shipment matching query does not exist.')  

    def assertEqualShipment(self, shipment, item):
        self.assertEqual(shipment.id, item['id'])
        self.assertEqual(shipment.shipping_address, item['shipping_address'])
        self.assertEqual(shipment.biling_address, item['biling_address'])
        self.assertEqual(shipment.product_price, Decimal(item['product_price']))
        self.assertEqual(shipment.delivery_cost, Decimal(item['delivery_cost']))
        self.assertEqual(shipment.final_price, Decimal(item['final_price']))
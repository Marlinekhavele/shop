from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product
import pdb;

class ProductAccountTests(APITestCase):

    def test_create_product(self):

        url = reverse('product-list')
        data = {'title': 'beast'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'beast')
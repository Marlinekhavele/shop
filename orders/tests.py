from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Customer
from products.models import  Product
from orders.models import Order

class OrderTests(APITestCase):

    def setUp(self):
        self.small_margatita = Product.objects.create(
            title="Small Margarita",
            description='A small Margarita for 100',
            price=100
        )
      

        self.customer = Customer.objects.create(name='kris',email='kris@gmail.com')


    def test_order_creation(self):
        url = reverse('create-order')
        data = {
            'customer': self.customer.id,
            'order_items':[
                {
                    'quantity': 1,
                    'product': self.small_margatita.id
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().status, 'draft')

    def test_order_updating_to_disallowed_status_raises_error(self):
        order = Order.objects.create(customer=self.customer)
        url = reverse('orders-get-delete-update',kwargs={'id':order.id})
        data = {'status':'delivered'}
        response = self.client.patch(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

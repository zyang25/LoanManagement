from django.test import TestCase
from django.contrib.auth import get_user_model
from customer.models import Customer
from rest_framework.test import APIClient, force_authenticate
from django.urls import reverse
from rest_framework import status
# Create your tests here.

Account = get_user_model()

class CustomerTestCase(TestCase):
    
    def setUp(self):
        self.c = APIClient()
        # URL
        self.create_url = reverse('customer-list')
        self.detail_url = reverse('customer-detail', kwargs={'id': 1})

        Account.objects.create(email='zyang678@gmail.com', password='testing')
        auth_user = Account.objects.get(email='zyang678@gmail.com')
        self.c.force_authenticate(user=auth_user)

        self.customer_data = {'fullname':'Zi','cell':'5166957250'}

        # Create testing Customer
        Customer.objects.create(fullname='testing', cell='5166957253')
    
    def get_customer_count(self):
        return Customer.objects.count()
    
    def test_create_customer_withauth(self):
        response = self.c.post(self.create_url, self.customer_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_customer_withoutauth(self):
        self.c.force_authenticate(user=None)
        response = self.c.post(self.create_url, self.customer_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_customer_withauth(self):
        udpated_name = 'Zi is updating it'
        updated_customer_data = {'fullname': udpated_name}
        res = self.c.put(self.detail_url, updated_customer_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        c = Customer.objects.get(cell='5166957253')
        self.assertEqual(c.fullname, udpated_name)

    def test_delete_customer_withauth(self):
        res = self.c.delete(self.detail_url)
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)



        







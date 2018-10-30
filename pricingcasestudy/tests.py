from django.contrib.auth.models import User
from django.test import TransactionTestCase, Client
from django.urls import reverse
from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_status_code_404_anonymous_user(self):
        response = self.client.get('pricingcasestudy/')
        self.assertEquals(response.status_code, 404)

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class SignUpPageTests(TestCase):

    def setUp(self):
        self.username = 'newuser'
        self.email = 'test@email.com'

    def test_sign_up_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)


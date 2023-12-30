from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN)
from rest_framework.test import APIClient

from product.utils.samples import sample_product


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.product = sample_product(title="Test")

        self.superuser = get_user_model().objects.create(email="test_api_superuser@example.com", is_superuser=True)
        self.superuser.set_password("qwerty1234")
        self.superuser.save()

        self.user = get_user_model().objects.create(email="test_api@example.com")
        self.user.set_password("qwerty1234")
        self.user.save()

    def tearDown(self):
        self.client.logout()

    def test_product_list(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(reverse("api:product_list"))

        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_product_list_no_access(self):
        result = self.client.get(reverse("api:product_list"))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_category_list_forbidden(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(reverse("api:category_list"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)

    def test_category_list(self):
        self.client.force_authenticate(user=self.superuser)

        result = self.client.get(reverse("api:category_list"))
        self.assertEqual(result.status_code, HTTP_200_OK)

import unittest
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class TestAuthCustomer(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.user_password = "12345678"

        self.user = get_user_model().objects.create(email="customer@example.com")
        self.user.set_password(self.user_password)
        self.user.save()

        self.manager_password = "qwerty12345"
        self.manager = get_user_model().objects.create(email="manager@example.com")
        self.manager.set_password(self.manager_password)
        self.manager.save()

    def test_user_login_wrong_email(self):
        user_login = self.client.login(email="wrong_email", password=self.user_password)
        self.assertFalse(user_login)

    def test_user_login_wrong_password(self):
        user_login = self.client.login(email=self.user.email, password="wrong_password")
        self.assertFalse(user_login)

    def test_user_access_admin_panel(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertEquals(response.status_code, HTTPStatus.FOUND)

    def test_manager_access_admin_panel(self):
        self.client.force_login(self.manager)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    @unittest.skip("We don't have index page, we will add it in week 35")
    def test_user_access_index_pae(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("index"))
        self.assertEquals(response.status_code, HTTPStatus.FOUND)

    @unittest.expectedFailure
    def test_user_access_index_page_failure_example(self):
        self.client.force_login(self.manager)
        response = self.client.get(reverse("admin:index"))
        self.assertEquals(response.status_code, HTTPStatus.IM_A_TEAPOT)

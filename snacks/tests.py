from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnackTests(TestCase):
    @staticmethod
    def create_snack_to_test():
        purchaser = get_user_model().objects.create(
            username="alex", password="alex8888")
        Snack.objects.create(name="Testcase", purchaser=purchaser, description="this is a test.")

    def test_snacks_list_200(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_snacks_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_not_used_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        snacks = response.context['object_list']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[2].name, "candy")
        self.assertEqual(snacks[2].description, "Yummy candy, good snack")
        self.assertEqual(snacks[2].purchaser.username, "alex")

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item


class ItemAPITests(APITestCase):

    def setUp(self):
        self.item = Item.objects.create(
            name="Test Item",
            description="This is a test item."
        )
        self.list_url = reverse('item-list')
        self.detail_url = reverse('item-detail', kwargs={'pk': self.item.pk})

    def test_create_item(self):
        data = {
            'name': 'New Item',
            'description': 'A description for new item.'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(Item.objects.last().name, 'New Item')

    def test_get_item_list(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)

    def test_get_single_item(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_update_item(self):
        updated_data = {
            'name': 'Updated Item',
            'description': 'Updated description'
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_delete_item(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)

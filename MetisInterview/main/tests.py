from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_fail_on_db_doesnt_exist(self):
        """
        this test will always fail as a testing settings.py and db needs to be created
        (django stops you from accessing the regular db in a test)
        """
        url = reverse('main:facts', kwargs={"table_name":'NonExistingTableName'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
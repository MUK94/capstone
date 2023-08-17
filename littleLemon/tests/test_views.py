from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

class MenuViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.menu_item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        cls.menu_item2 = Menu.objects.create(title="Pizza", price=150, inventory=50)
        
    def test_getAll(self):
        url = reverse('menu')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        serialized_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data
        
        self.assertEqual(response.data, serialized_data)
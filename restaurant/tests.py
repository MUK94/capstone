from django.test import TestCase
from .models import Menu
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from .serializers import MenuSerializer


class TestMenu(TestCase):
    @classmethod    
    def setUpTestData(cls):
        cls.item = Menu.objects.create(title="IceCream", price=80, inventory=100) 

    def test_item_title(self):
        self.assertEqual(self.item.title, "IceCream")
        
    def test_item_price(self):
        self.assertEqual(self.item.price, 80)
        
    def test_item_inventory(self):
        self.assertEqual(self.item.inventory, 100)
        
class MenuViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.menu_item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        cls.menu_item2 = Menu.objects.create(title="Pizza", price=150, inventory=50)
        
    def test_getAll(self):
        # self.client.force_authenticate(user=self.user)
        url = reverse('menu')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        serialized_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data
        
        self.assertEqual(response.data, serialized_data)
        
        
        
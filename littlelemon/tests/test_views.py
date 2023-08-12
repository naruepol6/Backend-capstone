from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
  def setUp(self) -> None:
    self.client = Client()
    self.user = User.objects.create_user(
        username='testuser',
        password='testpassword'
    )
    
    self.pizza = Menu.objects.create(title='Spaghetti', price=7.00, inventory=10)
    self.burger = Menu.objects.create(title='Burger', price=8.00, inventory=5)
    self.pasta = Menu.objects.create(title='Salad', price=5.00, inventory=15)

  def loginAsTestUser(self) -> None:
    self.client.login(username='testuser', password='testpassword')
    
  def test_getall(self):
    self.loginAsTestUser()
    response = self.client.get(reverse('menu'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    self.assertEqual(response.data, serializer.data)
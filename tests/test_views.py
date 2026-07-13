from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test records
        self.item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.item2 = Menu.objects.create(Title="Salad", Price=45, Inventory=50)
        
        # Initialize the API client
        self.client = APIClient()
        
        # Create and authenticate a test user to bypass the IsAuthenticated check if active globally
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.force_authenticate(user=self.user)

    def test_getall(self):
        # Fetch data via the endpoint
        response = self.client.get('/restaurant/menu/')
        
        # Serialize the database data manually
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Assert response match
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
from rest_framework import serializers 
from .models import Menu
from .models import Booking

class MenuSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Menu 
        fields = ['id', 'Title', 'Price', 'Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
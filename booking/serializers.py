from rest_framework import serializers

from booking.models import Booker, Hotel, Room, Booking


class BookerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


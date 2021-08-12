from rest_framework import viewsets, permissions

from booking.models import Hotel, Booker, Room, Booking
from booking.serializers import BookerSerializer, HotelSerializer, RoomSerializer, BookingSerializer


class BookerViewSet(viewsets.ModelViewSet):
    queryset = Booker.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookerSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookingSerializer
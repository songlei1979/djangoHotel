from rest_framework import routers

from booking.api import BookerViewSet, HotelViewSet, RoomViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register('api/Booker', BookerViewSet, 'Booker')
router.register('api/Hotel', HotelViewSet, 'Hotel')
router.register('api/Room', RoomViewSet, 'Room')
router.register('api/Booking', BookingViewSet, 'Booking')

urlpatterns = router.urls
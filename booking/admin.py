from django.contrib import admin

# Register your models here.
from booking.models import Booker, Hotel, Room, Booking

admin.site.register(Booker)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Booker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    passport = models.CharField(max_length=100)
    flightNumber = models.CharField(max_length=10)
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=6, choices=genders)

class Hotel(models.Model):
    name = models.CharField(max_length=50, default="")
    streetAddress = models.CharField(max_length=50)
    suburb = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    roomNum = models.CharField(max_length=10)
    roomtypes = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
        ('Quad', 'Quad'),
        ('Queen', 'Queen'),
        ('King', 'King'),
        ('Twin', 'Twin'),
        ('Double-double', 'Double-double'),
        ('Studio', 'Studio'),
    )
    roomtype = models.CharField(max_length=13, choices=roomtypes)

class Booking(models.Model):
    booker = models.ForeignKey(Booker, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    startDate = models.DateField()
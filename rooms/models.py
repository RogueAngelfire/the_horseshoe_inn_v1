from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Room(models.Model):

    name = models.CharField(max_length=254)
    size = models.IntegerField(default=0)
    description = models.TextField()
    breakfast_included = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def is_available_on_date(self, date_to_check):
        bookings = self.booking.filter(checkin_date__gte = date_to_check, checkout_date__lt=date_to_check)

        if len(bookings) == 0:
            return True 

        else:
            return False


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    checkin_date = models.DateField()
    checkout_date = models.DateField()

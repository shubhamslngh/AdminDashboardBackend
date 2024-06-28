from django.conf import settings
from django.db import models
from packages.models import Package

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('canceled', 'Canceled')])

    def __str__(self):
        return f'{self.user.username} - {self.package.name}'

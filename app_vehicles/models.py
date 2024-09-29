from django.db import models

class Vehicle(models.Model):
    title = models.CharField(max_length=60)
    vehicle_type = models.CharField(max_length=60)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    rent_end_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return '{} (id={})'.format(self.title, self.id)
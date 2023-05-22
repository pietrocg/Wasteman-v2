from django.db import models
from django.contrib.auth.models import User

class TrashItem(models.Model):
    photo = models.ImageField(upload_to='trash_photos')
    description = models.TextField()
    location = models.ForeignKey('UserLocation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trash Item - {self.id}"

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Location - {self.id}"

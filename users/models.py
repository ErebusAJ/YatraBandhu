from django.contrib.auth.models import User
from PIL import Image
from django.db import models

class user(User):
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
class TravelPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField(null=True)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)
    additional_info = models.TextField(blank=True)
    CATEGORIES_CHOICES = [
        ('Must See Attractions', 'Must See Attractions'),
        ('Hidden Gems', 'Hidden Gems'),
        ('Shopping', 'Shopping'),
        ('Great Food', 'Great Food'),
        ('Cultural Heritage', 'Cultural Heritage'),
        ('Art and Theater', 'Art and Theater'),
    ]
    categories = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, null=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.location} - {self.date_from} to {self.date_to}"
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics', blank=True,null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True,null=True)

    
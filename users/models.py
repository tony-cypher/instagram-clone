from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='users/%Y/%m/%d', default='blank-profile-picture.png')

    def __str__(self):
        return self.user.username
    
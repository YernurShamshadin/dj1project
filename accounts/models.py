from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    birthdate = models.DateField(default='2001-01-01')
    photo = models.ImageField(upload_to="user_photo/")

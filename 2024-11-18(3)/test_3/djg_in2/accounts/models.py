from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']




class Announcement(models.Model):
    announcement_title = models.CharField(max_length=50)
    announcement_content = models.CharField(max_length=255)
    announcement_important = models.BooleanField()
    created_at=models.DateField(auto_now=True)

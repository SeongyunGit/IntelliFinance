from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    member_birth = models.DateField(null=False, blank=False)
    pass


from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255, unique=True)
    phone = models.CharField(null=True,max_length=255)
    REQUIRED_FIELDS = [ 'phone', 'first_name', 'last_name']




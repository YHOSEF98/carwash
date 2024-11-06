from django.contrib.auth.models import AbstractUser, BaseUserManager
from api.models import Company
from django.db import models

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
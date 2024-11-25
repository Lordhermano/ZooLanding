from django.db import models
from django.contrib.auth.models import AbstractUser


class ZooUser(AbstractUser):
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    
    
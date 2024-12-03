from django.db import models
from django.contrib.auth.models import AbstractUser
from ZooAdmin import settings


class ZooUsers(models.Model):
    srno = models.AutoField(primary_key=True,auto_created=True)
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    email = models.EmailField(max_length=200,blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    
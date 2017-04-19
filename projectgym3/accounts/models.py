from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=1,
    choices=(
        ('F','여자'),('M','남자')
    ),default = 'M')
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)


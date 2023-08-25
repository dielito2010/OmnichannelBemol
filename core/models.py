from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cep = models.CharField(max_length=10, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    address_number = models.IntegerField(blank=True, null=True)
    channel_id_load = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
    
#from django.db import models
from django.contrib.auth.models import AbstractUser
from djongo import models as djongo_models

class CustomUser(AbstractUser, djongo_models.Model):
    # Campos adicionais que você deseja adicionar
    cep = djongo_models.TextField(null=False, blank=False)

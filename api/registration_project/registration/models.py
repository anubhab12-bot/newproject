from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password = None):
        if not email:
            return ValueError("The field is empty ")
        email = self.normalize_email(email)
        user = self.model(email = email)
        
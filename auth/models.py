from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
  pass



class User(AbstractBaseUser):
  email = models.EmailField()
  first_name = models.CharField()
  last_name = models.CharField()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
  
  

class AccessToken(models.Model):
  ACTIONS = [
    ('reset-password', 'Reset Password'),
    ('verify-email', 'Verify Email'),
  ]
  
  id = models.AutoField(primary_key=True)
  token = models.CharField()
  user = models.ForeignKey()
  action = models.CharField(choices=ACTIONS)
  created_at = models.DateTimeField()
  
  

class ApiToken(models.Model):
  id = models.AutoField()
  key = models.CharField()
  name = models.CharField()
  user = models.ForeignKey()
  created_at = models.DateTimeField()
  updated_at = models.DateTimeField()
  
  

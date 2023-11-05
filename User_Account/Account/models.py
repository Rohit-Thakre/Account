from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    number = models.CharField(max_length=10, null= True)
    avatar = models.ImageField(upload_to='profile_pic', null=True, default='avatar.jpg')
    email = models.EmailField(unique=True)
    
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
    

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return 

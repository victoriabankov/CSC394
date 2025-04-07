from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
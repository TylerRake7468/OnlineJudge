from django.db import models

# Create your models here.

class User(models.Model):
	UserId = models.AutoField(primary_key=True)
	Password = models.CharField(max_length=50)
	UserName = models.CharField(max_length=255)
	Email = models.CharField(max_length=255)
	DOB = models.DateField()
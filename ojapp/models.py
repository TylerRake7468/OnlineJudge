from django.db import models

# Create your models here.

class User(models.Model):
	UserId = models.AutoField(primary_key=True)
	Password = models.CharField(max_length=50)
	UserName = models.CharField(max_length=255)
	Email = models.CharField(max_length=255)
	DOB = models.DateField()

	def __str__(self):
		return self.UserName

class Problem(models.Model):
	DIFFICULTY_CHOICES = (
			('easy', 'Easy'),
			('medium', 'Medium'),
			('hard', 'Hard')
		)
	id = models.AutoField(primary_key=True)
	number = models.CharField(max_length=50)
	difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
	title = models.CharField(max_length=255)
	statement = models.TextField()
	tags = models.CharField(max_length=255)
	example_input = models.TextField()
	example_output = models.TextField()

	def __str__(self):
		return self.title
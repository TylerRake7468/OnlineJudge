from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class User(models.Model):
	UserId = models.AutoField(primary_key=True)
	Password = models.CharField(max_length=255)
	UserName = models.CharField(max_length=255)
	Email = models.CharField(max_length=255)

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
	statement = models.TextField(default="")
	constraints = models.TextField(default="")
	tags = models.CharField(max_length=255)
	example_input = models.TextField(default="")
	example_output = models.TextField(default="")
	example_explain = models.TextField(default="")

	def __str__(self):
		return self.title

	def safe_constraints(self):
		return mark_safe(self.constraints)

	def safe_statement(self):
		return mark_safe(self.statement)

	def safe_input(self):
		return mark_safe(self.example_input)

	def safe_output(self):
		return mark_safe(self.example_output)
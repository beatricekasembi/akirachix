from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	phone_number = models.CharField(max_length=20)
	subject = models.CharField(max_length=20)
	profession = models.CharField(max_length=20)
	company = models.CharField(max_length=20)
	experience = models.CharField(max_length=20)
	date_joined = models.DateField()
	id_number = models.SmallIntegerField()

	def __str__(self):
		return self.first_name

# Create your models here.

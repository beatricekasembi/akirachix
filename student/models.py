from django.db import models
from course.models import Course
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import datetime


class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=20)
	registration_number = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	phone_number = models.CharField(max_length=20)
	date_joined = models.DateField()
	Courses = models.ManyToManyField(Course, blank=True, related_name="students")
	# image = models.ImageField(upload_to = "profile_pictures", blank=True)

	def __str__(self):
		return self.first_name

	def full_name(self):
		return "{} {}".format(self.first_name, self.last_name)


	def calculate_age(self):
		today = datetime.date.today()
		return today.year - self.date_of_birth.year - ((today.month,today.day) < (self.date_of_birth.month, self.date_of_birth.day))

	age = property(calculate_age)

	def clean(self):
		age = self.age
		if age > 30 or age < 17:
			raise ValidationError("Age should be below 30 yrs and above 17 yrs to enroll")
		return age

	

# Create your models here.

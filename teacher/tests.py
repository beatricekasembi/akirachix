from django.test import TestCase
import datetime
from .models import Teacher
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse


class AddTeacherTestCase(TestCase):
	def setUp(self):
		self.data={
		"first_name":"Veronica",
		"last_name":"Thamaini",
		"gender":"female",
		"email":"veronica@gmail.com",
		"phone_number":"0785963789",
		"subject":"lifeskills",
		"profession":"consultant",
		"company":"Akirachix",
		"experience":"6yrs",
		"id_number":33617877,
		"date_joined":datetime.date.today(),
		}

		self.bad_data={
		"first_name":"Veronica",
		"last_name":"Thamaini",
		"gender":"female",
		"email":"veronicagmail.com",
		"phone_number":"07859",
		"subject":"lifeskills",
		"profession":"consultant",
		"company":"Akirachix",
		"experience":"6yrs",
		"id_number":33617877,
		"date_joined":datetime.date.today(),
		}

	def test_teacher_form_accepts_valid_data(self):
		form = TeacherForm(self.data)
		self.assertTrue(form.is_valid())


	def test_teacher_form_rejects_invalid_data(self):
		form = TeacherForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_teacher_view(self):
		client = Client()
		url = reverse("add_teacher")
		response = client.post(url,self.data)
		self.assertEqual(response.status_code,200)

	def test_add_teacher_view_bad(self):
		client = Client()
		url = reverse("add_teacher")
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code,400)


# Create your tests here.

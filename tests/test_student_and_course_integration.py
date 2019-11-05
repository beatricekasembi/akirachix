from django.test import TestCase
from student.models import Student 
from course.models import Course
from teacher.models import Teacher
import datetime


# class StudentCourseTestCase(TestCase):
# 	def setUp(self):
# 		self.student_a=Student.objects.create(
# 			first_name="Beatrice",
# 			last_name="Kasembi",
# 			date_of_birth=datetime.date(1996,12,4),
# 			gender="female",
# 			registration_number="1234",
# 			email="kasembibeatrice@gmail.com",
# 			phone_number="0791863939",
# 			date_joined=datetime.date.today(),
# 			)
# 		self.student_b=Student.objects.create(
# 			first_name="James",
# 			last_name="Mutua",
# 			date_of_birth=datetime.date(1998,8,5),
# 			gender="male",
# 			registration_number="5678",
# 			email="jamesmutua@gmail.com",
# 			phone_number="0714974243",
# 			date_joined=datetime.date.today(),
# 			)
# 		self.python=Course.objects.create(
# 			name="python",
# 			duration=3,
# 			start_date=datetime.date.today(),
# 			end_date=datetime.date.today(),
# 			description="This course is a technical course",
# 			)
		
# 		self.html=Course.objects.create(
# 			name="html",
# 			duration=2,
# 			start_date=datetime.date.today(),
# 			end_date=datetime.date.today(),
# 			description="This is my favourite course",
# 			)
		
# 		self.javascript=Course.objects.create(
# 			name="javascript",
# 			duration=3,
# 			start_date=datetime.date.today(),
# 			end_date=datetime.date.today(),
# 			description="I am currently learning js",
# 			)
		
# 	def test_student_can_join_a_course(self):
# 		self.student_a.Courses.add(self.python)
# 		self.assertEqual(self.student_a.Courses.count(),1)
# 		self.student_a.Courses.add(self.html)
# 		self.assertEqual(self.student_a.Courses.count(),2)
# 		self.student_a.Courses.add(self.javascript)
# 		self.assertEqual(self.student_a.Courses.count(),3)

# 	def test_student_can_join_many_courses(self):
# 		self.student_b.Courses.add(self.python,self.javascript,self.html)
# 		self.assertEqual(self.student_b.Courses.count(),3)



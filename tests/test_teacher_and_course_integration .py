from django.test import TestCase
from student.models import Student 
from course.models import Course
from teacher.models import Teacher
import datetime


class TeacherCourseTestCase(TestCase):
	def setUp(self):
		self.teacher_a=Teacher.objects.create(
			first_name="Jeff",
			last_name="Muthondu",
			gender="male",
			email="muthondu@gmail.com",
			phone_number="0785958789",
			subject="html",
			profession="creative director",
			company="Akirachix",
			experience="12yrs",
			id_number=20617877,
			date_joined=datetime.date.today(),
			)
		self.teacher_b=Teacher.objects.create(
			first_name="James",
			last_name="Mwai",
			gender="male",
			email="smartemwa@gmail.com",
			phone_number="0785963740",
			subject="python",
			profession="software engineer",
			company="Akirachix",
			experience="10yrs",
			id_number=22617877,
			date_joined=datetime.date.today(),
			)
		self.python=Course.objects.create(
			name="python",
			duration=3,
			start_date=datetime.date.today(),
			end_date=datetime.date.today(),
			description="This course is a technical course",
			)
		
		self.html=Course.objects.create(
			name="html",
			duration=2,
			start_date=datetime.date.today(),
			end_date=datetime.date.today(),
			description="This is my favourite course",
			)
		
		self.javascript=Course.objects.create(
			name="javascript",
			duration=3,
			start_date=datetime.date.today(),
			end_date=datetime.date.today(),
			description="I am currently learning js",
			)
		
	

	def test_teacher_can_train_a_course(self):
       self.python.teacher = self.teacher_b
       self.assertEqual(self.python.teacher, self.teacher_b)


   def test_teacher_can_train_many_courses(self):
       self.python.teacher = self.teacher_b
       self.html.teacher = self.teacher_b
       self.assertEqual(self.html.teacher,self.python.teacher)


 #   	def test_teacher_can_train_a_course(self):
	# 	self.course_a.Courses.add(self.python)
	# 	self.assertEqual(self.teacher_a.Courses.count(),1)
	# 	self.course_a.Courses.add(self.html)
	# 	self.assertEqual(self.teacher_a.Courses.count(),2)
	# 	self.course_a.Courses.add(self.javascript)
	# 	self.assertEqual(self.teacher_a.Courses.count(),3)

	# def test_teacher_can_train_many_courses(self):
	# 	self.student_b.Courses.add(self.python,self.javascript,self.html)
	# 	self.assertEqual(self.student_b.Courses.count(),3)
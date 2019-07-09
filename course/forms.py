from django import forms 
from.models import Course

class CourseForm(forms.ModelForm):

	class Meta:

		model = Course

 # creating a form module
		fields = "__all__"
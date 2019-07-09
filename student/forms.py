from django import forms 
from.models import Student

class StudentForm(forms.ModelForm):

	class Meta:

		model = Student

 # creating a form module
		fields = "__all__"     


	                

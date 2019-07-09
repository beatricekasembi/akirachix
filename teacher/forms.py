from django import forms 
from.models import Teacher

class TeacherForm(forms.ModelForm):

	class Meta:

		model = Teacher

 # creating a form module
		fields = "__all__"    
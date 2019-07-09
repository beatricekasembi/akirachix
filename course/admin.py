from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","duration",)
	search_fields = ("name","teacher__first_name","duration",)

admin.site.register(Course,CourseAdmin)


# Register your models here.

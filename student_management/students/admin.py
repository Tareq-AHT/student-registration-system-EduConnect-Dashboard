from django.contrib import admin
from django import forms
from .models import Student, Course, Enrollment


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'duration': forms.TextInput(attrs={'autocomplete': 'off'}),
            'instructor': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('name', 'price', 'duration', 'instructor') 


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'courses', 'payment_method', 'total_amount', 'timestamp')
    list_filter = ('payment_method', 'timestamp')
    search_fields = ('student_name', 'courses')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password') 
    search_fields = ('name', 'email')
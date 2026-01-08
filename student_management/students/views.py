from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import StudentRegistrationForm
from .models import Course, Enrollment, Student
from django.shortcuts import render, redirect
from django.contrib import messages


def register_view(request):
    success_message = None 
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():        
            name = form.cleaned_data['name']
            email = form.cleaned_data['email'].lower() 
            password = form.cleaned_data['password']
            Student.objects.create(name=name, email=email, password=password)
            success_message = f"Thank you {name}! Your information has been saved successfully."
            form = StudentRegistrationForm()  
    else:
        form = StudentRegistrationForm()  
    return render(request, 'students/registration.html', {'form': form, 'success_message': success_message})


def student_list_view(request):
    all_students = Student.objects.all() 
    return render(request, 'students/student_list.html', {'students': all_students})


def enroll_view(request):
    courses = Course.objects.all()
    return render(request, 'students/enrollment.html', {'courses': courses})



@csrf_exempt
def save_enrollment(request):
    if request.method == "POST":
        s_name = request.POST.get('student_name')
        c_names = request.POST.get('course_names')
        p_method = request.POST.get('payment_method')
        t_price = request.POST.get('total_price')

        if s_name and c_names:
            try:
                Enrollment.objects.create(
                    student_name=s_name,
                    courses=c_names,
                    payment_method=p_method,
                    total_amount=float(t_price) if t_price else 0.0
                )
                messages.success(request, f"Enrollment successful for {s_name}!")
            except Exception as e:
                messages.error(request, f"Error: {e}")
        
        return redirect('enrollment')
    return redirect('enrollment')

        
def enrolled_students_list(request):
    enrolled_data = Enrollment.objects.all().order_by('-timestamp')
    return render(request, 'students/enrolled_list.html', {'enrolled_data': enrolled_data})

def index_view(request):
    return render(request, 'students/index.html')




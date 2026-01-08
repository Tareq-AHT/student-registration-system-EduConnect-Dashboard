"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from students import views 



urlpatterns = [
    path('', views.index_view, name='index'),
    path('admin/', admin.site.urls), 
    path('register/', views.register_view, name='register'),
    path('enrollment/', views.enroll_view, name='enrollment'),
    path('list/', views.student_list_view, name='student_list'),
    path('save-enrollment/', views.save_enrollment, name='save_enrollment'),
    path('enrolled-list/', views.enrolled_students_list, name='enrolled_list'),
]


from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Student


# Create your views here.

class StudentListView(ListView):
    model = Student



#default template is student_list.html
#default object variable is student_list
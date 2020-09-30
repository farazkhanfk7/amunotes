from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Faculty,Department

# Create your views here.
def home(request):
    return render(request,'index.html')

class FacultyListView(ListView):
    model = Faculty
    template_name = "faculties.html"

class FacultyView(DetailView):
    model = Department
    template_name = "science.html"

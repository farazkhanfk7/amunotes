from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Faculty,Department

# Create your views here.
def home(request):
    return render(request,'index.html')

def facultylist(request):
    object_list = Faculty.objects.all()
    return render(request,'faculties.html',{'object_list':object_list})

def faculty(request,slug):
    if slug=='science':
        object_list = Department.objects.filter(faculty_name='science')
        return render(request,'science.html',{'object_list':object_list})
    elif slug=='lifescience':
        object_list = Department.objects.filter(faculty_name='lifescience')
        return render(request,'life_science.html',{'object_list':object_list})
    elif slug=='engg':
        # object_list = Department.objects.filter(faculty_name='engg')
        # return render(request,'engg.html',{'object_list':object_list})
        return HttpResponse("ERROR 404. Engineering Faculty page not found")
    else:
        return HttpResponse("ERROR 404. Faculty page not found")

class department(DetailView):
    model = Department
    template_name = "csd.html"

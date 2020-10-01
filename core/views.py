from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Faculty,Department,Subject,Notes

# Create your views here.
def home(request):
    return render(request,'index.html')

def facultylist(request):
    object_list = Faculty.objects.all()
    return render(request,'faculties.html',{'object_list':object_list})

# def faculty(request,slug):
#     if slug=='science':
#         object_list = Department.objects.filter(faculty_name='science')
#         return render(request,'science.html',{'object_list':object_list})
#     elif slug=='lifescience':
#         object_list = Department.objects.filter(faculty_name='lifescience')
#         return render(request,'life_science.html',{'object_list':object_list})
#     elif slug=='engg':
#         # object_list = Department.objects.filter(faculty_name='engg')
#         # return render(request,'engg.html',{'object_list':object_list})
#         return HttpResponse("ERROR 404. Engineering Faculty page not found")
#     else:
#         return HttpResponse("ERROR 404. Faculty page not found")

class faculty(DetailView):
    model = Faculty
    template_name = "departmentlist.html"

    def get_object(self, queryset=None):
        obj = super(DetailView, self).get_object(queryset=queryset)
        faculty = obj.get_faculty()
        return faculty

    def get_context_data(self, **kwargs):
        faculty_name = self.get_object()
        context = super(DetailView, self).get_context_data(**kwargs)
        context['departments'] = Department.objects.filter(facultycode=faculty_name)
        context['faculty'] = Faculty.objects.get(slug=faculty_name)
        return context
    

class department(DetailView):
    model = Department
    template_name = "departmentdetail.html"

    def get_object(self, queryset=None):
        obj = super(DetailView, self).get_object(queryset=queryset)
        code = obj.get_code()
        return code

    def get_context_data(self, **kwargs):
        code = self.get_object()
        context = super(DetailView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.filter(departmentcode=code)
        context['department'] = Department.objects.get(slug=code)
        return context

class document(DetailView):
    model = Subject
    template_name = "document.html"

    def get_object(self, queryset=None):
        obj = super(DetailView, self).get_object(queryset=queryset)
        subjectcode = obj.get_code()
        return subjectcode

    def get_context_data(self, **kwargs):
        subjectcode = self.get_object()
        context = super(DetailView, self).get_context_data(**kwargs)
        context['notes'] = Notes.objects.filter(slug=subjectcode)
        return context


def testing(request):
    dep = Department()
    code = dep.get_code()
    return HttpResponse(code)

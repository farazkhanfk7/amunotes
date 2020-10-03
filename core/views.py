from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Faculty,Department,Subject,Notes
from core.forms import NoteForm,SearchForm,ClassSearchForm,ClassUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/')
def uploadfile(request):
    if request.method == 'POST':
        form = NoteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'File Upload Successful !')
            return render(request,'upload.html',{'form':form})

    else:
        form = NoteForm()
        return render(request,'upload.html',{'form':form})

def search_class(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            depname = form.cleaned_data.get('department')
            data = Subject.objects.filter(department=depname)
            # return HttpResponse(depname)
            return render(request,'search.html',{'form':form,'depname':depname,'data':data})
        else:
            return HttpResponse("Error in form")
    else:
        form = SearchForm()
        return render(request,'search.html',{'form':form})

@login_required(login_url='/')
def updateclass(request):
    if request.method == 'POST':
        searchform = ClassSearchForm(request.POST)
        updateform = ClassUpdateForm(request.POST)
        if searchform.is_valid() and updateform.is_valid():
            # to get subjectname
            subject_name_full_str = searchform.cleaned_data.get('subject')
            subject_name_full_str = str(subject_name_full_str)
            subjectcode_slug = subject_name_full_str.split("(")[1].split(")")[0].lower()
            #to get starttime,stoptime and meetllink
            starttime = updateform.cleaned_data.get('starttime')
            stoptime = updateform.cleaned_data.get('stoptime')
            meetlink = updateform.cleaned_data.get('meetlink')
            b = Subject.objects.get(slug=subjectcode_slug)
            b.starttime = starttime
            b.stoptime = stoptime
            b.meetlink = meetlink
            b.save()
            messages.add_message(request, messages.INFO, 'Successfully Updated class details!')
            return redirect("updateclass")
        else:
            messages.add_message(request, messages.INFO, 'Error while updating')
            return render(request,'updateclass.html',{'searchform':searchform,'updateform':updateform})
    else:
        searchform = ClassSearchForm()
        updateform = ClassUpdateForm()
        return render(request,'updateclass.html',{'searchform':searchform,'updateform':updateform})
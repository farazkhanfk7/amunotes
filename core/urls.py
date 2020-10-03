from django.contrib import admin
from django.urls import path,include
from . import views
from .views import department,faculty,document
urlpatterns = [
    path('',views.home,name="home"),
    path('facultylist',views.facultylist,name="facultylist"),
    path('faculty/<slug>/',faculty.as_view(), name="faculty"),
    path('department/<slug>',department.as_view(),name="department"),
    path('subject/<slug>',document.as_view(),name="subject"),
    path('uploadfile',views.uploadfile,name="uploadfile"),
    path('search_class',views.search_class,name="search_class"),
    path('updateclass',views.updateclass,name="updateclass")
]
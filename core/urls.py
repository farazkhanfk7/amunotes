from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('facultylist',views.facultylist,name="facultylist"),
    path('faculty/<slug>/',views.faculty, name="faculty")
]
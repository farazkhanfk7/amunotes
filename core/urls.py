from django.contrib import admin
from django.urls import path,include
from . import views
from .views import FacultyListView, FacultyView
urlpatterns = [
    path('',views.home,name="home"),
    path('facultylist',FacultyListView.as_view(),name="facultylist"),
    path('faculty/<slug>/',FacultyView.as_view(), name="faculty")
]
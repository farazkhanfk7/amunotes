from django.contrib import admin
from django.urls import path,include
from . import views
from .views import department
urlpatterns = [
    path('',views.home,name="home"),
    path('facultylist',views.facultylist,name="facultylist"),
    path('faculty/<slug>/',views.faculty, name="faculty"),
    path('department/<slug>',department.as_view(),name="department")
]
from django.contrib import admin
from . models import Faculty,Department,Subject,Notes

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Notes)

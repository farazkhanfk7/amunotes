from django.db import models
from django.shortcuts import reverse

DEPARTMENT_SUBCODES = (
    ('csd', 'ccb'),
    ('maths', 'mmb')
)

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    facultycoverimg = models.ImageField(upload_to='faculty')
    img = models.ImageField(upload_to='faculty')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_faculty(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("faculty", kwargs={'slug': self.slug })

class Department(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,default=1)
    facultycode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='faculty')
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_code(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("department", kwargs={'slug': self.slug })

class Subject(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=1)
    departmentcode = models.CharField(max_length=100)
    subjectcode = models.CharField(max_length=100)
    subjectname = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return self.subjectcode

    def get_code(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("subject", kwargs={'slug': self.slug })


class Notes(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,default=1)
    topic = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    docs = models.FileField(upload_to='docs')
    slug = models.SlugField()

    def __str__(self):
        return self.topic

    def get_subject(self):
        return self.slug

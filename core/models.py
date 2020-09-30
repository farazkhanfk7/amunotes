from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='faculty')
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("faculty", kwargs={'slug': self.slug })

class Department(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,default=1)
    faculty_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='faculty')
    slug = models.SlugField()

    def __str__(self):
        return self.name
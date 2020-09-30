from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='faculty')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name} Faculty'

    def get_absolute_url(self):
        return reverse("core:faculty", kwargs={'slug': self.slug })

class Department(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='faculty')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name} Department'

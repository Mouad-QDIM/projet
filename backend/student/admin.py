from django.contrib import admin
from .models import Student, Module, Speciality

# Register your models here.
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Speciality)

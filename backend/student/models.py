from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.first_name+' '+self.last_name

    def update_student(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.save()

    def delete_student(self):
        self.delete()

class Speciality(models.Model):
    name = models.TextField()
    SEMESTER_CHOICES = [
        (1, ' 2 semesters'),
        (2, ' 4 semesters'),
        (3, ' 6 semesters')
    ]
    semesters = models.IntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.name

class Module(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.TextField()
    SEMESTER_CHOICES=[
        (1, ' semester 1'),
        (2, ' semester 2'),
        (3, ' semester 3'),
        (4, ' semester 4'),
        (5, ' semester 5'),
        (6, ' semester 6')
    ]
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    grade = models.FloatField(null=True, default=0)
    result = models.TextField(default='fail')

    def __str__(self):
        return str(self.grade)



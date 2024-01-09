from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Speciality, Module

# Create your views here.
def add_student(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        if fname and lname and age:
            student = Student(first_name=fname, last_name=lname, age=age)
            student.save()
        else:
            error_message = "please complete all fields."
            return render(request, 'student/add.html', {'error_message': error_message})
    return render(request, 'student/add.html')

def list_student(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students': students})

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.first_name = request.POST['fname']
        student.last_name = request.POST['lname']
        student.age = request.POST['age']
        if student.first_name and student.last_name and student.age:
            student.save()
            return redirect('list_student')
        else:
            error_message = "please complete all fields."
            return render(request, 'student/update.html', {'error_message': error_message, 'student': student})
    return render(request, 'student/update.html', {'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.module_set.all().delete()
    student.delete()
    return redirect('list_student')


def add_speciality(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        semesters = request.POST.get('semesters')

        if name and semesters:
            speciality = Speciality(name=name, semesters=semesters)
            speciality.save()
        else:
            error_message = "please complete all fields."
            return render(request, 'speciality/add.html', {'error_message': error_message})

    return render(request, 'speciality/add.html')

def list_speciality(request):
    specialities = Speciality.objects.all()
    return render(request, 'speciality/list.html', {'specialities': specialities})

def delete_speciality(request, speciality_id):
    speciality = get_object_or_404(Speciality, pk=speciality_id)
    speciality.delete()
    return redirect('list_speciality')


def update_speciality(request, speciality_id):
    speciality = get_object_or_404(Speciality, pk=speciality_id)
    if request.method == 'POST':
        speciality.name = request.POST['fname']
        speciality.semesters = request.POST['semesters']
        if speciality.name and speciality.semesters:
            speciality.save()
            return redirect('list_speciality')
        else:
            error_message = "please complete all fields."
            return render(request, 'speciality/update.html', {'error_message': error_message, 'speciality': speciality})
    return render(request, 'speciality/update.html', {'speciality': speciality})


def add_module(request):
    specialities = Speciality.objects.all()
    students = Student.objects.all()
    print(specialities)
    if request.method == 'POST':
        name = request.POST.get('name')
        speciality_id = request.POST.get('speciality')
        semester = request.POST.get('semester')
        student_id = request.POST.get('student')
        grade = request.POST.get('grade')
        result = request.POST.get('result')

        speciality = get_object_or_404(Speciality, id=speciality_id)
        student = get_object_or_404(Student, id=student_id)

        if name and speciality and semester and student and grade and result:
            module = Module(name=name, speciality=speciality,
                            semester=semester, student=student,
                            grade=grade, result=result)
            module.save()
        else:
            error_message = "please complete all fields."
            return render(request, 'module/add.html', {'error_message': error_message, 'specialities': specialities, 'students': students})

    return render(request, 'module/add.html', {'specialities': specialities, 'students': students})

def list_module(request):
    modules = Module.objects.all()
    return render(request, 'module/list.html', {'modules': modules})

def delete_module(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    module.delete()
    return redirect('list_module')


def update_module(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    specialities = Speciality.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        speciality_id = request.POST.get('speciality')
        semester = request.POST.get('semester')
        student_id = request.POST.get('student')
        grade = request.POST.get('grade')
        result = request.POST.get('result')

        speciality = get_object_or_404(Speciality, id=speciality_id)
        student = get_object_or_404(Student, id=student_id)

        if name and speciality and semester and student and grade and result:
            module.name = name
            module.speciality = speciality
            module.semester = semester
            module.student = student
            module.grade = grade
            module.result = result
            module.save()
            return redirect('list_module')
        else:
            error_message = "Please complete all fields."
            return render(request, 'module/update.html', {'error_message': error_message, 'module': module, 'specialities': specialities, 'students': students})

    return render(request, 'module/update.html', {'module': module, 'specialities': specialities, 'students': students})

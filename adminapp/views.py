from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import *
from .models import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='adminapp:login_page')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedras()
    subjects = services.get_subjects()
    teachers = services.get_teachers()
    groups = services.get_groups()
    students = services.get_students()

    context = {
        'counts': {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),
        }
    }
    return render(request, 'index.html', context=context)


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'adminapp:home_page'
            return redirect(next_url)

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('adminapp:home_page')


# FACULTY
@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:faculty_list')
    context = {
        'form': form,
    }
    return render(request, 'faculty/form.html', context=context)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:faculty_list')
    context = {
        'form': form,
    }
    return render(request, 'faculty/form.html', context=context)


@require_POST
@login_required_decorator
def faculty_delete(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    faculty.delete()
    return redirect('adminapp:faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    context = {
        'faculties': faculties,
    }
    return render(request, 'faculty/list.html', context=context)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:kafedra_list')
    context = {
        'form': form,
    }
    return render(request, 'kafedra/form.html', context=context)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:kafedra_list')
    context = {
        'form': form,
    }
    return render(request, 'kafedra/form.html', context=context)


@require_POST
@login_required_decorator
def kafedra_delete(request, pk):
    kafedra = Kafedra.objects.get(pk=pk)
    kafedra.delete()
    return redirect('adminapp:kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedras()
    context = {
        'kafedras': kafedras,
    }
    return render(request, 'kafedra/list.html', context=context)


# SUBJECT
@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:subject_list')
    context = {
        'form': form,
    }
    return render(request, 'subject/form.html', context=context)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:subject_list')
    context = {
        'form': form,
    }
    return render(request, 'subject/form.html', context=context)

@require_POST
@login_required_decorator
def subject_delete(request, pk):
    subject = Subject.objects.get(pk=pk)
    subject.delete()
    return redirect('adminapp:subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subjects()
    context = {
        'subjects': subjects,
    }
    return render(request, 'subject/list.html', context=context)


# TEACHER
@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:teacher_list')
    context = {
        'form': form,
    }
    return render(request, 'teacher/form.html', context=context)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:teacher_list')
    context = {
        'form': form,
    }
    return render(request, 'teacher/form.html', context=context)


@require_POST
@login_required_decorator
def teacher_delete(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()
    return redirect('adminapp:teacher_list')


@login_required_decorator
def teacher_list(request):
    teachers = services.get_teachers()
    context = {
        'teachers': teachers,
    }
    return render(request, 'teacher/list.html', context=context)


# GROUP
@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:group_list')
    context = {
        'form': form,
    }
    return render(request, 'group/form.html', context=context)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:group_list')
    context = {
        'form': form,
    }
    return render(request, 'group/form.html', context=context)


@require_POST
@login_required_decorator
def group_delete(request, pk):
    group = Group.objects.get(pk=pk)
    group.delete()
    return redirect('adminapp:group_list')


@login_required_decorator
def group_list(request):
    groups = services.get_groups()
    context = {
        'groups': groups,
    }
    return render(request, 'group/list.html', context=context)


# STUDENT
@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:student_list')
    context = {
        'form': form,
    }
    return render(request, 'student/form.html', context=context)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('adminapp:student_list')
    context = {
        'form': form,
    }
    return render(request, 'student/form.html', context=context)


@require_POST
@login_required_decorator
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('adminapp:student_list')


@login_required_decorator
def student_list(request):
    students = services.get_students()
    context = {
        'students': students,
    }
    return render(request, 'student/list.html', context=context)

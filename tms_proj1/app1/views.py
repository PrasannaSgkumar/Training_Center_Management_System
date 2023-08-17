from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect, HttpResponse
from app1.forms import  AddCourseForm, AddStaffsForm, AddStudentsForm, AddSubjectsForm, CreateUserForm
def index(re):
    return render(re, 'index.html')

def Courses(re):
    return render(re, 'courses.html')

def StudentsSignIN(re):
    return render(re, 'students-sign.html')

def adminsign(re):
    return render(re, 'adminsign.html')

def staffsign(re):
    return render(re, 'staff.html')
def staffdash(re):
    return render(re, 'staffdash.html')

def studentsdash(re):
    return render(re, 'studentsdashboard.html')



def addcourse(re):
    form=AddCourseForm()
    if re.method=='POST':
        form = AddCourseForm(re.POST)
        # print("printing post:", re.POST)
        if form.is_valid():
            form.save()
            return redirect('')


    context={'form':form}
    return render(re, 'addcourse.html', context)

def Staffsadd(re):
    form=AddStaffsForm()
    if re.method=='POST':
        form=AddStaffsForm(re.POST)
        if form.is_valid():
            form.save()
            return redirect('')


    context={'form':form}
    return render(re, 'addstaff.html', context)

def addstudents(re):

    form=AddStudentsForm()
    if re.method=='POST':
        print(re.POST)
        form=AddStudentsForm(re.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    context={'form':form}
    return render(re, 'addstudent.html', context)
def sub(re):
    form=AddSubjectsForm()
    if re.method=='POST':
        form=AddStudentsForm(re.POST)
        print(re.POST)

    context={'form':form}
    return render(re, 'addsubs.html', context)


def register(re):
    form=CreateUserForm()
    if re.method=='POST':
        form = CreateUserForm(re.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(re, 'addadmin.html', context)



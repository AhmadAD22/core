from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import Student
from ..forms.student import *
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password



def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('student:student_list')
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'student/create.html', context)


def update_student(request,id):
    student=get_object_or_404(Student,pk=id)
    if request.method=='POST':
        form=StudentUpdateForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
        else:
            context = {
                'form': form,
                'id':student.id   
                       }
            return render(request, 'student/update.html', context)
    form=StudentUpdateForm(instance=student)
    context={'form':form,
             'id':student.id 
             }
    return render(request,'student/update.html',context)

def student_list(request):
    students=Student.objects.all()
    context={
        'students':students
    }
    return render(request,'student/list.html',context)


def student_change_password(request,id):
        student=get_object_or_404(Student,id=id)
        password=request.POST['password']
        student.password=make_password(password)
        student.save()
        return redirect('student:update-student',id)

def delete_student(request,id):
     student=get_object_or_404(Student,id=id)
     student.delete()
     return redirect('student:student_list')
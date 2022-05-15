from django.shortcuts import render , redirect
from .forms import  StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required , permission_required

@login_required
def getStudents(request):
    students = Student.objects.all()
    return render(request , 'fbvApp/listStudent.html',{'students':students})
# Create your views here.

@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')
    return render(request,'fbvApp/createStudent.html', {'form':form})

@login_required
@permission_required('fbvApp.delete_student')
def deleteStudent(request , id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/list')
@login_required
def updateStudent(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance= student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            return redirect('/list')
    return render(request, 'fbvApp/update.html',{'form':form})


def logout(request):
    return render(request, 'fbvApp/logout.html')
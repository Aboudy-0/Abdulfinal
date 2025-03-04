from django.shortcuts import render, redirect, get_object_or_404
from Hospitalapp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def department(request):
    return render(request,'department.html')

def doctors(request):
    return render(request,'doctors.html')

def contacts(request):
    if request.method == "POST":
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/contacts')
    else:
        return render(request, 'contacts.html')

def appointment(request):
    if request.method == "POST":
        myappointment = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'])
        myappointment.save()
        return redirect('/show')
    else:
        return render(request, 'appointment.html')

def show(request):
    all = Appointment.objects.all()
    return  render(request,'show.html',{'all':all})

def delete(request,id):
    deletedappointment = Appointment.objects.get(id=id)
    deletedappointment.delete()
    return redirect('/show')

def edit(request,id):
    editinfo = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        editinfo.name = request.POST.get('name')
        editinfo.email = request.POST.get('email')
        editinfo.phone = request.POST.get('phone')
        editinfo.date = request.POST.get('date')
        editinfo.department = request.POST.get('department')
        editinfo.doctor = request.POST.get('doctor')
        editinfo.message = request.POST.get('message')
        editinfo.save()
        return redirect('/show')

    else:

        return render(request,'edit.html',{'editinfo':editinfo})

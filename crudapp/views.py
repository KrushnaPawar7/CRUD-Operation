from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def crud(request):
    return HttpResponse("good morning crud")

def create(request):
    print('my current method is', request.method)
    if request.method=="POST":
        nm=request.POST["ename"]
        sal=request.POST["esalary"]
        pos=request.POST["eposition"]
        bg=request.POST["ebloodgroup"]
        ag=request.POST["eage"]
        
        print(nm,sal,pos,bg,ag)
        
        
        emp=Employee.objects.create(name=nm,salary=sal,position=pos,blood_g=bg,age=ag)
        emp.save()
        return redirect("/show")
    return render(request,"create.html")

def show(request):
    emp=Employee.objects.all()
    context={}
    context["data"]=emp

    return render(request,"table.html",context)

def delete(request,rid):
    emp=Employee.objects.filter(id=rid)
    emp.delete()

    return redirect("/show")

def edit(request,pid):
    if request.method=="GET":
       emp=Employee.objects.filter(id=pid)
       context={}
       context["data"]=emp
       return render (request,"edit.html",context)
    else:
        nm=request.POST["ename"]
        sal=request.POST["esalary"]
        pos=request.POST["eposition"]
        bg=request.POST["ebloodgroup"]
        ag=request.POST["eage"]
        
        emp=Employee.objects.filter(id=pid)
        emp.update(name=nm,salary=sal,position=pos,blood_g=bg,age=ag)
        return redirect("/show")
  
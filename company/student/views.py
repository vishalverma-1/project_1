from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import std


def myfun(request):
    return render(request,'run.html')


def myfun2(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        data=std.objects.create(name=name,email=email,mobile=mobile)
        data.save()
        return redirect('read')
    else:
        return render(request,'run1.html')
    

def read(request):
        data1=std.objects.all()
        return render(request,'read.html',{'data1':data1})


def delete(request,id):
     data2=std.objects.get(id=id)
     data2.delete()
     return redirect("read")


def edit(request,id):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        i=std.objects.filter(id=id).update(name=name,email=email,mobile=mobile)
        return redirect('read')  
    else:
        ed=std.objects.filter(id=id)
        return render(request,'edit.html',{'data':ed})

          
     
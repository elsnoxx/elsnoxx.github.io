from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department

# Create your views here.
def index(request):
    return render(request, 'index.html')

def zamestnanci_list(request):
    zamestnanci = Employee.objects.all()
    return render(request, 'zamestnanci_list.html', {'zamestnanci': zamestnanci})

def zamestnanec_detail(request, empno):
    zamestnanec = Employee.objects.get(empno=empno)
    return render(request, 'zamestnanec_detail.html', {'zamestnanec': zamestnanec})

def zamestnanec_add(request):
    if request.method == 'POST':
        ename = request.POST['ename']
        job = request.POST['job']
        hiredate = request.POST['hiredate']
        sal = request.POST['sal']
        comm = request.POST.get('comm', None)
        deptno = Department.objects.get(deptno=request.POST['deptno'])
        
        Employee.objects.create(
            ename=ename,
            job=job,
            hiredate=hiredate,
            sal=sal,
            comm=comm,
            deptno=deptno
        )
        return redirect('zamestnanci_list')
    
    return render(request, 'zamestnanec_form.html')

def zamestnanec_edit(request, empno):
    zamestnanec = Employee.objects.get(empno=empno)
    
    if request.method == 'POST':
        zamestnanec.ename = request.POST['ename']
        zamestnanec.job = request.POST['job']
        zamestnanec.mgr = request.POST.get('mgr', None)
        zamestnanec.hiredate = request.POST['hiredate']
        zamestnanec.sal = request.POST['sal']
        zamestnanec.comm = request.POST.get('comm', None)
        zamestnanec.deptno = Department.objects.get(deptno=request.POST['deptno'])
        
        zamestnanec.save()
        return redirect('zamestnanci_list')
    
    return render(request, 'zamestnanec_form.html', {'zamestnanec': zamestnanec})

def zamestnanec_delete(request, empno):
    zamestnanec = Employee.objects.get(empno=empno)
    if request.method == 'POST':
        zamestnanec.delete()
        return redirect('zamestnanci_list')
    
    return render(request, 'zamestnanec_confirm_delete.html', {'zamestnanec': zamestnanec})

def oddeleni_list(request):
    oddeleni = Department.objects.all()
    return render(request, 'oddeleni_list.html', {'oddeleni': oddeleni})

def oddeleni_detail(request, deptno):
    oddeleni = Department.objects.get(deptno=deptno)
    return render(request, 'oddeleni_detail.html', {'oddeleni': oddeleni})

def oddeleni_add(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        
        Department.objects.create(
            dname=dname
        )
        return redirect('oddeleni_list')
    
    return render(request, 'oddeleni_form.html')

def oddeleni_edit(request, deptno):
    oddeleni = Department.objects.get(deptno=deptno)
    
    if request.method == 'POST':
        
        oddeleni.dname = request.POST['dname']
        
        oddeleni.save()
        return redirect('oddeleni_list')
    
    return render(request, 'oddeleni_form.html', {'oddeleni': oddeleni})

def oddeleni_delete(request, deptno):
    oddeleni = Department.objects.get(deptno=deptno)
    if request.method == 'POST':
        oddeleni.delete()
        return redirect('oddeleni_list')
    
    return render(request, 'oddeleni_confirm_delete.html', {'oddeleni': oddeleni})


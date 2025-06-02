from django.db import models

# Create your models here.
class Department(models.Model):
    deptno = models.IntegerField(primary_key=True, auto_created=True)
    dname = models.CharField(max_length=50)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True, auto_created=True)
    ename = models.CharField(max_length=50)
    job = models.CharField(max_length=30)
    hiredate = models.DateField()
    sal = models.DecimalField(max_digits=10, decimal_places=2)
    comm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deptno = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
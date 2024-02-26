from django.db import models

# Create your views here.
class EmployeeCurrentPositioinModel(models.Model):
    positionTitle =models.CharField(max_length = 200)
    def __str__(self):
        return self.positionTitle
class EMployeeRegistrationsModel(models.Model):
    employeeName = models.CharField(max_length = 200)
    employeeAge = models.IntegerField(max_length = 2)
    employeeCode = models.CharField(max_length = 50)
    employeeCurrentPosition = models.ForeignKey(EmployeeCurrentPositioinModel, on_delete = models.CASCADE)
# Create your models here.

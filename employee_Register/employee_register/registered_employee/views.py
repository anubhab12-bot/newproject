from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import EMployeeRegistrationsModel
def EmployeeListView(request):
    context = {'employee_list' : EMployeeRegistrationsModel.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

def EmployeeFormViewList(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = EMployeeRegistrationsModel.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = EMployeeRegistrationsModel.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list') 
    
def DestroyEmployeeRecord(request, id):
    employe_DETAIL = EMployeeRegistrationsModel.objects.get(pk = id)
    employe_DETAIL.delete()
    return redirect('/employee/list')
        
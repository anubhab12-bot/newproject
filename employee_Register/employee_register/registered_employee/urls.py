from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.EmployeeFormViewList , name = 'employee_insert'),
    path('form/<int:id>/', views.EmployeeFormViewList,name='employee_update'),
    path('list/', views.EmployeeListView, name = 'employee_list'),
    path('delete/<int:id>', views.DestroyEmployeeRecord, name = 'employee_delete')
]

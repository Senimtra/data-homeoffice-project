from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name = 'home'),
   path('analysis', views.analysis, name = 'analysis'),
   path('employees', views.employees, name = 'employees'),
   path('companies', views.companies, name = 'companies'),
   path('employees/add', views.add_employee, name = 'add_employee')
]

from django.http import HttpResponse
from django.template import loader

def home(request):
   template = loader.get_template('home.html')
   return HttpResponse(template.render())

def analysis(request):
   template = loader.get_template('analysis.html')
   return HttpResponse(template.render())

def employees(request):
   template = loader.get_template('employees.html')
   return HttpResponse(template.render())

def companies(request):
   template = loader.get_template('companies.html')
   return HttpResponse(template.render())

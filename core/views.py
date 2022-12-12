### Imports ###
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employees
from django.db.models import Count

import json
import re

### Home view ###
def home(request):
   template = loader.get_template('home.html')
   return HttpResponse(template.render())

### Analysis view ###
def analysis(request):
   template = loader.get_template('analysis.html')
   age_groups = []; labels = []; data = []
   age_query = Employees.objects.values('age').annotate(count=Count('age')).order_by()
   for group in age_query:
      age_groups.append((re.findall('\d{2}', group['age'])[-1], group['age'], group['count']))
   age_groups = sorted(age_groups)
   labels = [label[1] for label in age_groups]
   data = [data[2] for data in age_groups]
   context = {'labels': json.dumps(labels), 'data': json.dumps(data)}
   return HttpResponse(template.render(context, request))

### Survey view ###
def survey(request):
   template = loader.get_template('survey.html')
   return HttpResponse(template.render({}, request))

### Add observation ###
def survey_add(request):
   gender = request.POST['gender']
   age = request.POST['age']
   children = request.POST['children']
   rural = request.POST['rural']
   executive = request.POST['executive']
   employees = request.POST['employees']
   wfh_days = request.POST['wfh_days']
   more_breaks = request.POST['more_breaks']
   wfh_day_condition = request.POST['wfh_day_condition']
   productivity = request.POST['productivity']
   entry = Employees(gender=gender, age=age, children=children, rural=rural, executive=executive, employees=employees, wfh_days=wfh_days, more_breaks=more_breaks, wfh_day_condition=wfh_day_condition, productivity=productivity)
   entry.save()
   return HttpResponseRedirect(reverse('home'))

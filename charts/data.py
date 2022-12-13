from core.models import Employees
from django.db.models import Count

import json
import re

### Employee happiness bar chart ###
def happiness():
   happiness = []; labels = []; data = []
   happiness_query = Employees.objects.values('wfh_day_condition').annotate(count = Count('wfh_day_condition'))
   for level in happiness_query:
      match level['wfh_day_condition']:
         case 'I feel great': level['rank'] = 1
         case 'I feel better': level['rank'] = 2
         case 'I feel like I always do': level['rank'] = 3
         case "I don't feel so good": level['rank'] = 4
         case 'I feel worse': level['rank'] = 5
   for entry in happiness_query:
      happiness.append((entry['rank'], entry['wfh_day_condition'], entry['count']))
   [(labels.append(el[1]), data.append(el[2])) for el in sorted(happiness)]
   context = {'happiness_labels': json.dumps(labels), 'happiness_data': json.dumps(data)}
   return context

### Employee productivity bar chart ###
def productivity():
   productivity = []; labels = []; data = []
   productivity_query = Employees.objects.values('productivity').annotate(count = Count('productivity'))
   for level in productivity_query:
      match level['productivity']:
         case "I'm a lot more productive": level['rank'] = 1
         case "I'm more productive": level['rank'] = 2
         case "I'm as productive as ever": level['rank'] = 3
         case "I'm less productive": level['rank'] = 4
         case "I'm a lot less productive": level['rank'] = 5
   for entry in productivity_query:
      productivity.append((entry['rank'], entry['productivity'], entry['count']))
   [(labels.append(el[1]), data.append(el[2])) for el in sorted(productivity)]
   context = {'productivity_labels': json.dumps(labels), 'productivity_data': json.dumps(data)}
   return context

### Age groups bar chart ###
def age_groups():
   age_groups = []; labels = []; data = []
   age_query = Employees.objects.values('age').annotate(count = Count('age'))
   for group in age_query:
      age_groups.append((int(re.findall('\d{2}', group['age'])[-1]), group['age'], group['count']))
   age_groups = sorted(age_groups)
   labels = [label[1] for label in age_groups]
   data = [data[2] for data in age_groups]
   context = {'age_groups_labels': json.dumps(labels), 'age_groups_data': json.dumps(data)}
   return context

### Company size donut chart ###
def company_size():
   company_size = []; labels = []; data = []
   company_query = Employees.objects.values('employees').annotate(count = Count('employees'))
   for size in company_query:
      company_size.append((int(re.findall('\d{1,3}', size['employees'])[0]), size['employees'], size['count']))
   company_size = sorted(company_size)
   labels = [label[1] for label in company_size]
   data = [data[2] for data in company_size]
   context = {'company_size_labels': json.dumps(labels), 'company_size_data': json.dumps(data)}
   return context

### Amount remote days bar chart ###
def remote_days():
   remote_days = []; labels = []; data = []
   days_query = Employees.objects.values('wfh_days').annotate(count = Count('wfh_days'))
   [remote_days.append((days['wfh_days'], days['count'])) for days in days_query]
   [(labels.append(days[0]), data.append(days[1])) for days in sorted(remote_days)]
   context = {'remote_days_labels': json.dumps(labels), 'remote_days_data': json.dumps(data)}
   return context

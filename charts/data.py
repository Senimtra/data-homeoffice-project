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

### More breaks pie chart ###
def breaks():
   labels = []; data = []
   break_query = Employees.objects.values('more_breaks').annotate(count = Count('more_breaks'))
   [(labels.append(yes_no['more_breaks']), data.append(yes_no['count'])) for yes_no in break_query]
   context = {'more_breaks_labels': json.dumps(labels), 'more_breaks_data': json.dumps(data)}
   return context

### Gender distribution pie chart ###
def gender():
   labels = []; data = []
   gender_query = Employees.objects.values('gender').annotate(count = Count('gender'))
   [(labels.append(option['gender']), data.append(option['count'])) for option in gender_query]
   context = {'gender_distribution_labels': json.dumps(labels), 'gender_distribution_data': json.dumps(data)}
   return context

### Age groups bar chart ###
def age_groups():
   age_groups = []; females = []; males = []
   age_query = Employees.objects.values('gender', 'age').annotate(count = Count('age'))
   for group in age_query:
      age_groups.append((int(re.findall('\d{2}', group['age'])[-1]), group['gender'], group['age'], group['count']))
   for group in age_groups:
      females.append(group) if group[1] == 'Female' else males.append(group)
   females = [group[3] for group in sorted(females)]
   males = [group[3] for group in sorted(males)]
   context = {'age_groups_females': json.dumps(females), 'age_groups_males': json.dumps(males)}
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
   remote_days = []; data = []
   rural_days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
   children_days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
   # Remote days total
   days_query = Employees.objects.values('wfh_days').annotate(count = Count('wfh_days'))
   [remote_days.append((days['wfh_days'], days['count'])) for days in days_query]
   [data.append(days[1]) for days in sorted(remote_days)]
   # Remote days children
   children_query = Employees.objects.filter(children = 'Yes').values('wfh_days').annotate(count = Count('wfh_days'))
   for entry in children_query:
      children_days[entry['wfh_days']] = entry['count']
   # Remote days rural
   rural_query = Employees.objects.filter(rural = 'Yes').values('wfh_days').annotate(count = Count('wfh_days'))
   for entry in rural_query:
      rural_days[entry['wfh_days']] = entry['count']
   # Set up context
   context = {'remote_days_data': json.dumps(data), 'remote_days_rural': json.dumps(list(rural_days.values())), 'remote_days_children': json.dumps(list(children_days.values()))}
   return context

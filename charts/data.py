from core.models import Employees
from django.db.models import Count

import json
import re

### Age groups donut chart ###
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
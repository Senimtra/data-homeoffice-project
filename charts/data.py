from core.models import Employees
from django.db.models import Count

import json
import re

### Age groups donut chart ###
def age_groups():
   print('haha')
   age_groups = []; labels = []; data = []
   age_query = Employees.objects.values('age').annotate(count=Count('age')).order_by()
   for group in age_query:
      age_groups.append((re.findall('\d{2}', group['age'])[-1], group['age'], group['count']))
   age_groups = sorted(age_groups)
   labels = [label[1] for label in age_groups]
   data = [data[2] for data in age_groups]
   context = {'labels': json.dumps(labels), 'data': json.dumps(data)}
   return context
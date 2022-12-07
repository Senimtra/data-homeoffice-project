from core.models import Employees
import csv

def run():
   with open('survey_employees.csv') as file:
      data = csv.reader(file)
      next(data)  # skip header
      Employees.objects.all().delete()
      for row in data:
         print(row)
         employee = Employees(gender = row[0],
                              age = row[1],
                              children = row[2],
                              rural = row[3],
                              executive = row[4],
                              employees = row[5],
                              wfh_days = row[6],
                              more_breaks = row[7],
                              wfh_day_condition = row[8],
                              productivity = row[9])
         employee.save()

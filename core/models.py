from django.db import models

class Employees(models.Model):
   gender = models.CharField(max_length = 23)
   age = models.CharField(max_length = 5)
   children = models.BooleanField()
   rural = models.BooleanField()
   executive = models.BooleanField()
   employees = models.CharField(max_length = 6)
   wfh_days = models.IntegerField()
   more_breaks = models.BooleanField()
   wfh_day_condition = models.CharField(max_length = 23)
   productivity = models.CharField(max_length = 25)

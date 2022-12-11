from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name = 'home'),
   path('analysis', views.analysis, name = 'analysis'),
   path('survey', views.survey, name = 'survey'),
   path('survey/add', views.survey_add, name = 'survey_add')
]

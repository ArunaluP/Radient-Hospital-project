from django.urls import path
from . import views

app_name = 'reminders'

urlpatterns = [
    path('makereminder/', views.makereminder, name='makereminder'),
    path('', views.viewreminder, name='viewreminders'),

]
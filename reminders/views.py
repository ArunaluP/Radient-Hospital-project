from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Reminder
from . import forms 

# Create your views here.
def viewreminder(request):
  reminders = Reminder.objects.all().values()
   
  template = loader.get_template('remind_list.html')
  context = {
    'reminders': reminders,
  }
  return HttpResponse(template.render(context, request))

def makereminder(request):
  if request.method == 'POST':
    form = forms.CreateReminder(request.POST)
    if form.is_valid():
      form.save()
      return redirect('reminders:viewreminders')
  else:
    form = forms.CreateReminder()
    template = loader.get_template('reminder.html')
    context = {
      'form': form,
    }
  return HttpResponse(template.render(context, request))
from django.db import models
import datetime


# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return (f"{self.title}")
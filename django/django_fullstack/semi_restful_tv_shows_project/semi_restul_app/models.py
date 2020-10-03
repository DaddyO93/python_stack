from __future__ import unicode_literals
from django.db import models
from datetime import date
# Create your models here.
class ShowManager (models.Manager):
    def basic_validator (self, reqPOST):
        errors = {}
        current_date = str(date.today())
        adjusted_current_date = current_date.strip("-")
        if len(reqPOST['title'])<2:
            errors['title'] = "Title must be at least 2 characters long"
        if len(reqPOST['network'])<3:
            errors['network'] = "Network must be at least 3 characters long"
        if len(reqPOST['desc'])>0 and len(reqPOST['desc'])<10:
            errors['desc'] = "The Description must be blank, or at least 10 characters long"
        for show in Show.objects.all():
            if reqPOST['title'] == show.title:
                errors ['title'] = "You must use a unique Title"
        if reqPOST['release_date']>adjusted_current_date or len(reqPOST['release_date'])==0:
            errors ['release_date'] = "You must select a date before today"
        return errors

class Show (models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=10)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
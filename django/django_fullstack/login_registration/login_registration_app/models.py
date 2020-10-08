from __future__ import unicode_literals
from django.db import models
import re
from datetime import date

# Create your models here.
class UserManager (models.Manager):
    def loginValidator(self, dataPost):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-z!-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(dataPost['first_name'])<2:
            errors['first_name'] = "First name must be longer than 2 characters"
        if len(dataPost['last_name'])<2:
            errors['last_name'] = "Last name must be longer than 2 characters"
        if len(dataPost['password'])<8:
            errors['password'] = "Password must be at least 8 characters. HINT: Use a phrase or sentence."
        # Determine if at least 13 years old
        b_day = dataPost['b_day']
        test_date = str(date.today().replace(year=date.today().year-13))
        if test_date<b_day:
            errors['b_day'] = "You must be at least 13 to register"
        # Ensure valid email address
        if not EMAIL_REGEX.match(dataPost['email']):
            errors['email'] = "You must use a valid email address"
        # Validate unique email address
        user = User.objects.filter(email=dataPost['email'])
        if len(user)>0:
            errors['email'] = "That email address is already taken"
        # Confirm password and pw_confirm match
        if dataPost['password'] != dataPost['pw_confirm']:
            errors['pw_confirm'] = "Your passwords did not match"
        return errors
        

class User (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    b_day = models.DateField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
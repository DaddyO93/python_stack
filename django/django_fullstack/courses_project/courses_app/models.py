from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager (models.Manager):
    def basic_validator (self, postDATA):
        errors = {}
        if len(postDATA['name'])<5:
            errors['name'] = "The course name must be longer than 5 characters long"
        if len(postDATA['desc'])<15:
            errors['desc'] = "A description must be longer than 15 characters"
        for course in Course.objects.all():
            if postDATA['name'] == course.name:
                errors['name'] = "Please use a unique Course name"
        return errors

class Course (models.Model):
    name = models.CharField(max_length=40) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description (models.Model):
    desc = models.TextField()
    course_name = models.OneToOneField(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    
class Comment (models.Model):
    comment = models.CharField(max_length=255)
    course_name = models.ForeignKey(Course, related_name='comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

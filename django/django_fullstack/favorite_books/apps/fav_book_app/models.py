from django.db import models
from apps.login_registration_app.models import User

# Create your models here.
class UserManager(models.Manager):
    def bookValidator (self, postData):
        errors = {}
        if len(postData['title'])<1:
            errors['title'] = "You must enter a title"
        title = Book.objects.filter(title=postData['title'])
        if len(title)>0:
            errors['title'] = "That book has already been entered"
        if len(postData['desc'])<5:
            errors['desc'] = "You must enter a description longer than 5 characters"
        return errors

class Book (models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
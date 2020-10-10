from django.db import models
from apps.login_registration_app.models import User

# Create your models here.
class Message (models.Model):
    message = models.TextField()
    commenter = models.ForeignKey(User, related_name="posted_messages", on_delete=models.CASCADE)
    comments = models.ManyToManyField(User, through="Comment", through_fields=("parent_message", "user"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment (models.Model):
    comment = models.TextField()
    parent_message = models.ForeignKey(Message, related_name="related_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
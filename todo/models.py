from django.db import models
# This line imports the user model from django authentication framework
# User model basically represents the user table in datbase
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    srno = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
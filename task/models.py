from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField(max_length=200)

    priority_type=(
        ("low","low"),
        ("medium","medium"),
        ("high","high"),

        )

    priority=models.CharField(max_length=200,choices=priority_type,default="low")

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)


    
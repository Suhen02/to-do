from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    values=models.CharField(max_length=100)
    priority=models.IntegerField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class Register(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    

    

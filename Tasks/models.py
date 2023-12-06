from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Supervisor(models.Model):
    name=models.CharField(max_length=50)
    
class Department(models.Model):
    title=models.TextField(max_length=50)
    supervisor=models.ForeignKey(Supervisor,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
class Ticket(models.Model):
    Priority_levels=(
        ('level 1','Critical'),
        ('level 3','Escalated'),
        ('level 5','Normal'),
        
    )
    description=models.CharField()
    created=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    priority=models.CharField(max_length=20,choices=Priority_levels)
    department=models.ForeignKey(Department,on_delete=models.PROTECT)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    

    def __str__(self):
        return 

class Technicaian(models.Model):
    name=models.CharField(max_length=50)
    tickets=models.ForeignKey(Ticket,on_delete=models.PROTECT)
    Supervisor=models.ForeignKey(Supervisor,on_delete=models.CASCADE)

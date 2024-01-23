from django.db import models
from django.conf import settings
# Create your models here.


class Supervisor(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    
class Department(models.Model):
    title=models.TextField(max_length=50)
    supervisor=models.ForeignKey(Supervisor,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
class Caller(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
        
class Technician(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
        
class Category(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return self.title
class Ticket(models.Model):
    Priority_levels=(
        ('level 1','Critical'),
        ('level 3','Escalated'),
        ('level 4','Planning'),
        ('level 5','Normal'),
        
    )
    Resolution=(
        ('resolved','Resolved'),
        ('on hold','On Hold'),
        ('awaiting more info','Awaiting Additional Info'),
        
    )
    Status=(
        ('unassigned','unassigned'),
        ('assigned','assigned'),
        ('resolved','resolved'),
    )
    description=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(Caller,on_delete=models.CASCADE)
    priority=models.CharField(max_length=20,choices=Priority_levels,blank=True, null=True)
    assigned=models.ForeignKey(Technician,on_delete=models.DO_NOTHING,blank=True, null=True,related_name='technicianassigned')
    # department=models.ForeignKey(Department,on_delete=models.PROTECT)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    resolved=models.CharField(max_length=30,choices=Resolution,blank=True, null=True)
    status=models.CharField(max_length=50,choices=Status,default='unassigned')  
    
class Messsage(models.Model):
    description=models.CharField(max_length=200)
    commeter=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='messages')    

    
    

   



from django.db import models
from Person.models import Person




class Task_type(models.Model):
    description=models.TextField(null=True)
    name = models.CharField(max_length=300,unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=300,unique=True)
    task_type=models.ForeignKey(Task_type,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Task_record(models.Model):
    STATUS = (
        ('queued'),
        ('running'),
        ('done'),
        ('failed'),
        ('rejected'),

    )
    Task_name = models.CharField(max_length=300, unique=True)   #to know arguments
    date_time=models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
    )
    arg1 = models.CharField(null=True, max_length=50)
    arg2 = models.CharField(null=True, max_length=50)
    arg3 = models.CharField(null=True, max_length=50)
    arg4 = models.CharField(null=True, max_length=50)
    arg5 = models.CharField(null=True, max_length=50)
    arg6 = models.CharField(null=True, max_length=50)

    person=models.ForeignKey(Person,on_delete=models.SET_NULL)



    def __str__(self):
        return 'Task :{} , date : {} , state : {}'.format(self.name, self.date_time,self.status)

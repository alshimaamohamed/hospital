from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from Places.models import Room,Reception,Department,Office,Hospital
from Tasks.models import Task,Task_record
fs = FileSystemStorage(location='/media/photos/person')



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(storage=fs)
    acessed_tasks=models.ManyToManyField(Task)
    class Meta:
        abstract = True


class Doctor(Person):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)


class Nurse(Person):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)



class Receptionist(Person):
   reception=models.ForeignKey(Reception,on_delete=models.CASCADE)




class Patient(Person):
    stay_room=models.ForeignKey(Room,on_delete=models.SET_NULL)


class Hospital_manager(Person):
   manager_office=models.OneToOneField(Office)
   manages=models.OneToOneField(Hospital)


class Department_manager(Person):
   manages=models.OneToOneField(Department,on_delete=models.CASCADE)



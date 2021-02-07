from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from Places.models import Room,Reception,Department,Office,Hospital
from Tasks.models import Task,Task_record
fs = FileSystemStorage(location='/media/photos/person/')



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(storage=fs)
    acessed_tasks=models.ManyToManyField(Task)



class Doctor(Person):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)


class Nurse(Person):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    start_shift=models.TimeField()
    end_shift=models.TimeField()


class Receptionist(Person):
   reception=models.ForeignKey(Reception,on_delete=models.CASCADE)




class Patient(Person):
    TYPE=(('male','male'),('female','female'),('child','child'))
    stay_room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    gender=models.CharField( max_length=32,
        choices=TYPE)
    age=models.IntegerField()
    mobile=models.IntegerField()
    nationality=models.CharField(max_length=100)
    

class Hospital_manager(Person):
   manager_office=models.OneToOneField(Office,on_delete=models.CASCADE)
   manages=models.OneToOneField(Hospital,on_delete=models.CASCADE)


class Department_manager(Person):
   manages=models.OneToOneField(Department,on_delete=models.CASCADE)


class Patient_Mate(Person):
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    mobile=models.IntegerField()


class Mesurements(models.Model):

    heart_rate = models.FloatField()
    tempreture=models.FloatField()
    pressure=models.FloatField()
    time_date=models.DateTimeField(auto_now=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)


    def __str__(self):
        return  'date: {} , heart rate : {} , Tempreture : {} '.format(self.time_date,self.heart_rate,self.tempreture)

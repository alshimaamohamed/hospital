from django.db import models
from django.core.files.storage import FileSystemStorage
from Places.models import Kitchen,Floor,Pharmacy
fs = FileSystemStorage(location='/media/photos/medicine')

class Anchor(models.Model):
    X_location=models.FloatField()
    Y_location=models.FloatField()


    def __str__(self):
        return 'x :{} , y : {} '.format(self.X_location, self.Y_location)


class Meal(models.Model):
    type=models.CharField(max_length=30)
    total_fats=models.FloatField()
    name=models.CharField(max_length=30)
    kitchen=models.ForeignKey(Kitchen)
    count=models.IntegerField()
    def __str__(self):
        return self.name

class Food_item(models.Model):
    name=models.CharField(max_length=30)
    fats_gram=models.FloatField()
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    image=models.ImageField(storage=fs)
    count=models.IntegerField()
    pharmacy=models.ForeignKey(Pharmacy,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



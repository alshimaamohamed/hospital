from django.db import models
#from Items.models import Anchor,Meal,Medicine

class Hospital(models.Model):
    name=models.CharField(max_length=300,unique=True)
    address=models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=300)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Floor(models.Model):
    number = models.IntegerField()
    building = models.ForeignKey(Building,on_delete=models.CASCADE)

    def __int__(self):
        return self.number

class Pharmacy(models.Model):
    name = models.CharField(max_length=300)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    main_anchor = models.ForeignKey(null=True,to='Items.Anchor',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    number = models.IntegerField(unique=True)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    main_anchor = models.ForeignKey(to='Items.Meal',on_delete=models.CASCADE)


    def __int__(self):
        return self.number

class Room(models.Model):
    TYPE = (
        ('single','single'),
        ('double','double'),
        ('triple','triple')

    )
    number = models.IntegerField(unique=True)
    type = models.CharField( max_length=32,
        choices=TYPE)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    main_anchor = models.ForeignKey(null=True,to='Items.Anchor',on_delete=models.CASCADE)
    avilibility=models.BooleanField(default=True)



    def __int__(self):
        return self.number

class Scan_lab(models.Model):
    number = models.IntegerField(unique=True)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    main_anchor = models.ForeignKey(null=True,to='Items.Anchor',on_delete=models.CASCADE)


    def __int__(self):
        return self.number

class Office(models.Model):
    number = models.IntegerField(unique=True)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    main_anchor = models.ForeignKey(null=True,to='Items.Anchor',on_delete=models.CASCADE)


    def __int__(self):
        return self.number




class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Charging_station(models.Model):
    number = models.IntegerField(unique=True)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    main_anchor = models.ForeignKey(null=True,to='Items.Anchor',on_delete=models.CASCADE)


    def __int__(self):
        return self.number



class Bio_labs(models.Model):
    number = models.IntegerField(unique=True)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)

    def __int__(self):
        return self.number


class Reception(models.Model):
    name = models.CharField(max_length=300)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

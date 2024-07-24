from django.db import models
# Create your models here.
class student(models.Model):
    usn=models.CharField(max_length=10)
    name=models.CharField(max_length=40)
    sem=models.IntegerField()
    def __str__(self):
        return self.usn+" "+self.name+" "+str(self.sem)
class Project(models.Model):
    studentname=models.CharField(max_length=200)
    ptopic=models.CharField(max_length=200)
    plangauges=models.CharField(max_length=200)
    pduration=models.IntegerField(help_text='Enter in days')
    def str (self):
        return self.ptopic
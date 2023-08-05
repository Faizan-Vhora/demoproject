from django.db import models

# Create your models here.
class student1(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    marks = models.IntegerField()
    address=models.TextField()
    class Meta:
        db_table='studentrecord'

class teacher(models.Model):
    student=models.ForeignKey(student1,on_delete=models.CASCADE)
    t_name = models.CharField(max_length=150)
    mo_no = models.IntegerField(max_length=10)
    address = models.TextField(null=True,blank=True)


class veggi(models.Model):
    i_name = models.CharField(max_length=150)
    record = models.IntegerField(max_length=10)
from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=18)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
    

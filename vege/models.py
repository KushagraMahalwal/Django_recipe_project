from django.db import models
from django.contrib.auth.models import User

# Create your models here. or Creating the database tables

class Receipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # here we are creating a user object which is build in in django
    # on delete =set null means when a user delete from the database then the values are set to null
    # on delete=set default and etc
    receipe_name=models.CharField(max_length=100)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to="recipe")

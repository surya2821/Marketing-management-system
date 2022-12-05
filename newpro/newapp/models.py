from django.db import models
class  App(models.Model):
    Firstname=models.CharField(max_length=64,null=False)
    lastname=models.CharField(max_length=32,null=False)
    email=models.CharField(max_length=64,null=False)
    password=models.CharField(max_length=64,null=False)
    mobilenumber = models.IntegerField(primary_key=True)


from django.db import models

# Create your models here.

class Registmodel(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    file=models.FileField(upload_to='bank_app/static')
    phone=models.IntegerField()
    pin=models.IntegerField()
    balance=models.IntegerField()
    ac=models.IntegerField()

class addmoney(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)

class withdrawmoney(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)


class newsmodel(models.Model):
    topic=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)

class wishlist(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField()
    topic=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    date=models.DateField()






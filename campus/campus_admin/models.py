from django.db import models
from datetime import datetime

# Create your models here.

class Login(models.Model):
	firstname=models.CharField(max_length=30)
	secondname=models.CharField(max_length=30)
	email=models.EmailField()
	contactnumber=models.IntegerField()
	college=models.TextField()
	place=models.TextField()
	password=models.TextField()
	account_type=models.CharField(max_length=5)
class Offers(models.Model):
	title=models.TextField()
	description=models.TextField()
	image=models.FileField(upload_to='offer')	
	date=models.DateField(default=datetime.now)
	time=models.TimeField(default=datetime.now)
	
class Posts(models.Model):
	title=models.TextField()
	description=models.TextField()
	image=models.FileField(upload_to='posts')
	date=models.DateField(default=datetime.now)
	time=models.TimeField(default=datetime.now)

class Points(models.Model):
	name=models.TextField()
	name_id=models.IntegerField()
	point=models.IntegerField()
	title=models.TextField()
	date=models.DateField(default=datetime.now)
	time=models.TimeField(default=datetime.now)

		
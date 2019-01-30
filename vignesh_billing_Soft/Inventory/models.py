from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Products(models.Model):
	Name=models.CharField(max_length=20)
	Description=models.TextField()
	Packaging=models.TextField()
	HSNCode=models.CharField(max_length=20)
	Batch=models.CharField(max_length=20)    
	Exp_Date=models.DateField('Expiry Date')
	qty=models.IntegerField()
	GST=models.FloatField(null=True,blank=True,default=None)

class Customers(models.Model):
	Name=models.CharField(max_length=20)
	Addr=models.TextField()
	Mobile=models.CharField(max_length=20)
	GST=models.CharField(max_length=30)
	Lic=models.CharField(max_length=30)
	Outstanding=models.IntegerField()
	Premium=models.BooleanField(default=0)
	
class Invoices(models.Model):
	Product_Name=models.CharField(max_length=30)
	Free=models.IntegerField()
	GST=models.FloatField(null=True,blank=True,default=None)
	Qty=models.IntegerField()
	Discount=models.FloatField(null=True,blank=True,default=None)
	Exp_Date=models.DateField('Expiry Date',default=None)
	Price=models.FloatField(null=True,blank=True,default=None)
	p_id=models.ForeignKey(Products)
	c_id=models.ForeignKey(Customers)

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


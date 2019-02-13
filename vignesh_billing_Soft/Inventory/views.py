from django.shortcuts import render
from Inventory.models import *
from django.http import JsonResponse
import json
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from django.core import serializers

# Create your views here.

def Product_list(request):
	Pnames = Products.objects.all().order_by('Name')
	Pdts={"Pdts": Pnames}
	return render( request, 'Inventory.html', Pdts)

def Add_products(request):
	product = Products()
	if request.method == 'POST':
		data=json.loads(request.body)
		obj = Products.objects.filter(Name=data['Name'],Batch=data['Batch'])
		if obj:
			for object in obj:
				object.Name = data['Name']
				object.Description = data['Desc']
				object.Packaging = data['Packaging']
				object.HSNCode = data['HSN']
				object.Batch = data['Batch']
				object.Exp_Date = data['Exp']
				object.qty = data['qty']
				object.GST = data['gst']
				object.MRP = data['MRP']
				object.save()
			data={'data':'Data Already Exists and updated'}
		else:
			product.Name=data['Name']
			product.Description = data['Desc']
			product.Packaging = data['Packaging']
			product.HSNCode = data['HSN']
			product.Batch = data['Batch']
			product.Exp_Date = data['Exp']
			product.qty = data['qty']
			product.GST = data['gst']
			product.MRP = data['MRP']
			product.save()
			data={'data':'Data Added Successfully'}
		return HttpResponseRedirect("Inventory.html",{"Pdts": Products.objects.all()})
	else:
		return render(request, 'Inventory.html', {"Pdts": Products.objects.all()})
	

def Delete_products(request):
	data = json.loads(request.body)
	if request.method == 'POST':
		obj = Products.objects.filter(Name=data['Name'],Batch=data['Batch'])
		for object in obj:
			object.delete()
		data={'data':'Data Deleted Successfully'}
	else:
		render(request, 'Inventory.html', {"Pdts": Products.objects.all()})	
	return JsonResponse(data)

def Search_products(request):
	# data = json.loads(request.body)
	Name=request.GET.get('search')
	if request.method == 'GET':
		obj = Products.objects.filter(Name__icontains=Name).order_by('Name')
		return render(request, 'Inventory.html', {"Pdts": obj})

def Filter_products(request):
	time_threshold = datetime.now() + timedelta(days=180)
	obj = Products.objects.filter(Exp_Date__lt=time_threshold)
	return render(request, "Inventory.html", {"Pdts": obj})

def Billing_view(request):
	return render(request, "Billing.html")

def Billing_Product(request):
	data=json.loads(request.body)
	if request.method == 'POST':	
		obj1 = Products.objects.filter(Name__icontains=data['Name']).order_by('Exp_Date')
		qty=0

		obj = Products.objects.filter(Name__icontains=data['Name']).order_by('Exp_Date').first()
		data=[0]*(4+len(obj1))
		data[0]=obj.Exp_Date
		data[1]=obj.GST
		data[2]=obj.MRP
		data[3]=obj.id
		K=1
		for i in obj1:
			data[3+K]=obj.qty
			K+=1

	return JsonResponse({"Data": data})

def Billing_products(request):
	obj=Products.objects.all().order_by('Name')
	data = [0]*len(obj)
	k=0
	for i in obj:
		data[k]=i.Name
		k+=1;
	return JsonResponse({"Data": data})

def Customer_products(request):
	if request.method == 'POST':
		data=json.loads(request.body)
		obj = Customers.objects.filter(Mobile=data['Mobile'])
		data = {}
		for i in obj:
			data.update({'Name': i.Name})
			data.update({'Addr': i.Addr})
			data.update({'Mobile': i.Name})
			data.update({'Name': i.Name})
			data['Name']=i.Name
			data['Addr']=i.Addr
			data['Mobile']=i.Mobile
			if i.Premium == "False":
				data.update({'Premium': "Non-Premium"})
			else:
				data.update({'Premium': "Premium"})
	return JsonResponse({"Data": data})

def Customers_List(request):
	Cnames = Customers.objects.all().order_by('Name')
	Cst={"Cst": Cnames}
	return render( request, 'Customers.html', Cst)

def Add_customers(request):
	customer = Customers()
	if request.method == 'POST':
		data=json.loads(request.body)
		obj = Customers.objects.filter(Name=data['Name'],Mobile=data['Mobile'])
		if obj:
			for object in obj:
				object.Name = data['Name']
				object.Addr = data['Addr']
				object.Mobile = data['Mobile']
				# object.GST = data['GST']
				# object.Lic = data['Lic']
				object.Outstanding = data['Outstanding']
				object.Premium = data['Prem']
				object.save()
			data={'data':'Data Already Exists and updated'}
		else:
			customer.Name=data['Name']
			customer.Addr = data['Addr']
			customer.Mobile = data['Mobile']
			# customer.GST = data['GST']
			# customer.Lic = data['Lic']
			customer.Outstanding = data['Outstanding']
			customer.Premium = data['Prem']
			customer.save()
			data={'data':'Data Added Successfully'}
		return HttpResponseRedirect("Customers.html", {"Cst": Customers.objects.all()})
	else:
		return render(request, 'Customers.html', {"Cst": Customers.objects.all()})
	

def Delete_customers(request):
	data = json.loads(request.body)
	if request.method == 'POST':
		obj = Customers.objects.filter(Name=data['Name'],Mobile=data['Mobile'])
		for object in obj:
			object.delete()
		data={'data':'Data Deleted Successfully'}
	else:
		render(request, 'Customers.html', {"Cst": Customers.objects.all()})	
	return JsonResponse(data)

def Search_customers(request):
	# data = json.loads(request.body)
	Name=request.GET.get('search')
	if request.method == 'GET':
		obj = Customers.objects.filter(Name__icontains=Name).order_by('Name')
		return render(request, 'Customers.html', {"Cst": obj})

def Filter_customers(request):
	obj = Customers.objects.filter(Premium="True")
	return render(request, "Customers.html", {"Cst": obj})
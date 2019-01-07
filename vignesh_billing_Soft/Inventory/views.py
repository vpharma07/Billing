from django.shortcuts import render
from Inventory.models import *
from django.http import JsonResponse
import json
from django.http import HttpResponseRedirect
# Create your views here.

def Product_list(request):
	print 'test'
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
			print "data"
		data={'data':'Data Deleted Successfully'}
	else:
		render(request, 'Inventory.html', {"Pdts": Products.objects.all()})	
	return JsonResponse(data)

def Search_products(request):
	# data = json.loads(request.body)
	Name=request.GET.get('search')
	if request.method == 'GET':
		obj = Products.objects.filter(Name__icontains=Name).order_by('Name')
		print obj
		Pdts={"Pdts": obj}
		print Pdts
		return render(request, 'Inventory.html', Pdts)
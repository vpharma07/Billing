from django.shortcuts import render
from Inventory.models import *
# Create your views here.
def Product_list(request):
	Pnames = Products.objects.all()
	return render( request, 'list.html', locals())


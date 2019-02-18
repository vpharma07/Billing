"""vignesh_billing_Soft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Inventory import views as inventory_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Inventory/$', inventory_views.Product_list),
    url(r'^Inventory/ajax/add_inventory/$', inventory_views.Add_products),
    url(r'^Inventory/ajax/delete_inventory/$', inventory_views.Delete_products),
    url(r'^Inventory/ajax/search_inventory/$', inventory_views.Search_products),
    url(r'^Inventory/ajax/filter_inventory/$', inventory_views.Filter_products),
    url(r'^Billing/$', inventory_views.Billing_view),
    url(r'^Billing/ajax/products$', inventory_views.Billing_products),
    url(r'^Billing/ajax/customers$', inventory_views.Customer_products),
    url(r'^Customers/$', inventory_views.Customers_List),
    url(r'^Customers/ajax/add_customer/$', inventory_views.Add_customers),
    url(r'^Customers/ajax/delete_customer/$', inventory_views.Delete_customers),
    url(r'^Customers/ajax/search_customer/$', inventory_views.Search_customers),
    url(r'^Customers/ajax/filter_customer/$', inventory_views.Filter_customers),
    url(r'^$', inventory_views.index),
    ]

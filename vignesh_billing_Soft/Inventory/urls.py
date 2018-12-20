from django.conf.urls import url
import views

urlpatterns = [
    url(r'^Inventory/', views.Product_list)
    #url('', Inventory.Product_list, name='Products'),
]
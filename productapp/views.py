import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, JsonResponse
from productapp.models import Product
from django.core import serializers
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
	return render(request,'productapp/product_index.html')


"""
function for json response for list
"""
def pro_list(request):
	if request.method =='GET':		
		data = serializers.serialize("json", Product.objects.all())
		# data = 	Product.objects.values()
		# print(data)
		# stud_data = list(data)
		
		data = {
		'pro': data,
		}		
		return JsonResponse({'satus':'ok','stud_data':data} )
	else:
		return JsonResponse({'status':0})

@login_required
def product_list(request):
	pro = Product.objects.all()[:20]
	# import pdb;pdb.set_trace()
	# context = {
	# 	'prosss':pro
	# }
	# test = 'test'
	return render(request,'productapp/home.html',{'pro':pro})



def mycart(request):
	if request.method=='GET':
		mylist = []
		cartid = request.GET.get('id')
		mylist.append(cartid)
		data = {
		'res':mylist
		}
		# import pdb;pdb.set_trace()
		return JsonResponse(data)


def cart_add(request, pk):
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.add(product=product)
    return redirect(reverse("productapp/index"))


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(reverse("productapp:cart_detail"))
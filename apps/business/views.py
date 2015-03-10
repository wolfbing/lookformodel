from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def business_profile(request):
	return render_to_response("business/business_profile.html")

def order_create(request):
	return render_to_response("business/order_create.html")

def order_manage(request):
	return render_to_response("business/order_manage.html")

def order_detail(request):
	return render_to_response("business/order_detail.html")

def collect(request):
	return render_to_response("business/collect.html")

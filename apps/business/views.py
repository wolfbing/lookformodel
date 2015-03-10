from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def business_profile(request):
	return render_to_response("business/business_profile.html")

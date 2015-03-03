from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

def model_list(request):
	return render_to_response("model/model_list.html")
	# template = "model/model_list.html"
    # context = {}
	# return render(request,template,context)

def model_detail(request):
	return render_to_response("model/detail.html")
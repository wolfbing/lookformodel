from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response



# def home(request):
#     return render_to_response("home/index.html")

def model_list(request):
	return render_to_response("model/model_list.html")
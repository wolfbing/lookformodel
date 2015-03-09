from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def about(request):
    return render_to_response("about/about.html")


def article_detail(request):
	return render_to_response("about/article_detail.html")
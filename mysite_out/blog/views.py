from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return HttpResponse('<h1>Hello World. You are reading my blog.</h1>')

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def name(request):
    return render (request, "name.html")
def group(request):
    return render (request, "group.html")
def age(request):
    return render (request, "age.html")
def common(request):
    return render (request, "common.html")
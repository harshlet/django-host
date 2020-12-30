from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def feature(request):
    return render(request,"feature.html")

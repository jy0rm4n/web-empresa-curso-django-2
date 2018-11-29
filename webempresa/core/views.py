from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/home.htm")


def about(request):
    return render(request, "core/about.htm")


def store(request):
    return render(request, "core/store.htm")

from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse("Hello")


def main_page(request):
    return render(request, "CyberSecurityApp/main.html", {"title": "Main page"})


def applications(request):
    return render(request, "CyberSecurityApp/applications.html", {"title": "Applications"})


def tips_and_tricks(request):
    return render(request, "CyberSecurityApp/tips_and_tricks.html", {"title": "Tips and tricks"})


def useful_sources(request):
    return render(request, "CyberSecurityApp/useful_sources.html", {"title": "Useful sources"})


def form(request):
    return render(request, "CyberSecurityApp/forms.html", {"title": "Form"})

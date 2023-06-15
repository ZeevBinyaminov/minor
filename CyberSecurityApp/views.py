from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, "CyberSecurityApp/main.html", {"title": "Main page", "one": "disabled"})


def tips_and_tricks(request):
    return render(request, "CyberSecurityApp/tips_and_tricks.html", {"title": "Tips and tricks", "two": "disabled"})


def useful_sources(request):
    return render(request, "CyberSecurityApp/useful_sources.html", {"title": "Useful sources", "three": "disabled"})


def applications(request):
    return render(request, "CyberSecurityApp/applications.html", {"title": "Applications", "four": "disabled"})


def form(request):
    return render(request, "CyberSecurityApp/forms.html", {"title": "Form", "five": "disabled"})


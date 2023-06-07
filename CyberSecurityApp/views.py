from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse("Hello")


def main_page(request):
    return render(request, "CyberSecurityApp/main.html", {"title": "Основная страница",
                                                          "text": "Текст основной страницы"})


def applications(request):
    return render(request, "CyberSecurityApp/applications.html", {"title": "Приложения",
                                                                  "text": "Приложения для пентестинга"})


def tips_and_tricks(request):
    return render(request, "CyberSecurityApp/tips_and_tricks.html", {"title": "Посказки и приемы",
                                                                     "text": "Про подсказки и приемы"})


def useful_resources(request):
    return render(request, "CyberSecurityApp/useful_resources.html", {"title": "Полезные источники",
                                                                    "text": "Про полезные источники"})

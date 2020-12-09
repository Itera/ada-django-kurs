from django.shortcuts import render


def index(request):
    return render(request, "cookbook/index.html")


def detail(request, recipe_id):
    return render(request, "cookbook/detail.html")

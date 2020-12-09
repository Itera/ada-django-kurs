from django.shortcuts import render

from .models import Recipe


def index(request):
    recipe_list = Recipe.objects.all()
    context = {"recipe_list": recipe_list}
    return render(request, "cookbook/index.html", context)

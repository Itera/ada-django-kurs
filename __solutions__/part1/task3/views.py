from django.shortcuts import render

from .models import Recipe


def index(request):
    # Legg til løsning for pub_date også?
    recipe_list = Recipe.objects.order_by("title")
    context = {"recipe_list": recipe_list}
    return render(request, "cookbook/index.html", context)

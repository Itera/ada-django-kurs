from django.shortcuts import get_object_or_404, render

from .models import Recipe


def index(request):
    recipe_list = Recipe.objects.order_by("title")
    context = {"recipe_list": recipe_list}
    return render(request, "cookbook/index.html", context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {"recipe": recipe}

    if request.method == "POST":
        recipe.likes += 1
        recipe.save()

    return render(request, "cookbook/detail.html", context)

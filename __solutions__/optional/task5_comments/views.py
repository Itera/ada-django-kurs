from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, Comment


def index(request):
    recipe_list = Recipe.objects.order_by("title")
    context = {"recipe_list": recipe_list}
    return render(request, "cookbook/index.html", context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {"recipe": recipe}
    return render(request, "cookbook/detail.html", context)


def comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {"recipe": recipe}

    if request.method == "POST":
        author = request.POST["author"]
        comment = request.POST["comment"]

        Comment.objects.create(author=author, comment=comment, recipe=recipe)

        return HttpResponseRedirect(reverse("cookbook:detail", args=(recipe.id,)))

    return render(request, "cookbook/comment.html", context)

# Task 5: Add comment section

Level of difficulty: **hard**.

As this is a more complicated task than the others, we will divide this task into two parts. The first part is easier than the second one, so you can finish after the first part if you would like to do other tasks instead.

## Step 1: Render the comments

The first thing you will have to do is to create a new model for comments.

Open `models.py` and create a new class named `Comment`. As with the `Recipe` model, our new class will also extend the `models.Model` class. We would like three fields in our `Comment` model:

- `comment`: _TextField_
- `author`: _TextField_
- `pub_date`: _DateTimeField_

Take a look at how these fields are used in the `Recipe` model, and reuse the same syntax in our new model. Additionally, we need a `recipe` field for connecting the comments to the correct recipe. This `recipe` field is called a foreign key, and works as a pointer to a given recipe. You can add the foreign key like this:

```python
recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
```

Once you have added all the fields, your `Comment` model should look like this:

```python
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
```

Next, we need to let our database know about the changes to our model. To do this, we create a _migration_, which describes the changes we have made. After we have created the migration, we apply the migration to let the database know about the changes.

First, click on the tab named `Shell` in the bottom right window in repl.it. Type the following into the shell, and press enter:

```python
python manage.py makemigrations cookbook
```

This command created a migration with the changes you have made. Further, we will apply the migration with the following command:

```python
python manage.py migrate cookbook
```

Type it into your shell, and press enter. Now you should see a message ending with `OK`. If not, ask an Itera employee for help.

The next step is to create a few comments we can display in our application. To do this, we will use the Django admin panel. This is a page where you, among other things, can see and edit all the content in your database. But, before we head over to the admin panel, we have to register our new `Comment` model such that we can access it through the admin panel.

Open `admin.py`, and import `Comment` from `.models`. As you can see, the `Recipe` model is already imported from there. Next, register the `Comment` model by adding this line:

```python
admin.site.register(Comment)
```

Head over to _/admin_. Log in with username _ada_ and password _lovelace_, and you will access the admin panel. Click on `Comments`, and then `Add comment` in the upper right corner. Choose the recipe you want to comment, type in author and your comment, and save the changes. Repeat this a few times such that we have some testdata.

Now it's time to render these comments in our application. Open `detail.html`, and add a `<h2>` tag with the text "Comments" in it. To render our comments, we will perform some magic.

Do you remember that we added recipe as a foreign key in our `Comment` model? This will make the retrieval of comments very easy for us! To retrieve all comments of a recipe, simply use the following syntax:

```python
recipe.comment_set.all
```

This will return a list of comments for the given recipe. Now, use a for-loop to iterate through the comment list and add display each comment with a `<p>` tag. Remember that you can access the different fields by using the syntax `[VARIABLE].comment`, `[VARIABLE].author` etc.

Stuck in the for-loop? Remember to ask an Itera employee for help or check out the `__solutions__` folder. Also, remember that you created such a for-loop in part 1 of the project, so you could also seek inspiration in `index.html`.

Head over to _/cookbook_. Navigate to one of the recipes you added a comment to. Hopefully, the comments will now have appeared in your application. Great job!

## Step 2: Create comments in the application

If we want to add a new comment, we have to access the admin panel and type it in there. Wouldn't it be easier if we could add the comments directly in the application? Let's fix that!

Open `urls.py` and insert a new path with the same format as the other two. Here's the information you need for constructing the path:

- We would like the path to be "\<int:recipe_id\>/comment".
- We are going to add a view in `views.py`, and the name of this view will be `comment`.
- We would like to use the name "comment" to refer to this path.

Did you manage to construct the new path? Remember to check out the `__solutions__` folder if you are stuck.

Next, open `views.py`. Now we will add the logic for posting new comments to our database.

Create a function `comment`, which contains exactly the same logic as `detail`, but the url in the render statement is _cookbook/comment.html_ instead of _cookbook/detail.html_. Further, add this code above the render statement:

```python
if request.method == "POST":
    author = request.POST["author"]
    comment = request.POST["comment"]

    Comment.objects.create(author=author, comment=comment, recipe=recipe)

    return HttpResponseRedirect(reverse("cookbook:detail", args=(recipe.id,)))
```

The code snippet works like this: if the request from the template is a POST request, i.e. that we want to modify something (for instance write to the database), then we extract the author and the comment values from the request. Next, we create a `Comment` object and use the author and comment as parameters. We also add the recipe here, as we need it for constructing the foreign key. Finally, we respond the POST request with a redirect to the detail view, where we send recipe.id as a parameter.

To make this codesnippet work, put these imports on the top of the file:

```python
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, Comment
```

The next step is to create a template (page) for registering comments. Add a new file in `templates/cookbook/` with the name `comment.html`. Copy this HTML structure and paste it into your file:

```html
{% load static %}

<html>
  <head>
    <link rel="stylesheet" href="{% static 'cookbook/style.css' %}" />
  </head>
  <body>
  
  </body>
</html>
```

First, add a `<h1>` heading inside the `<body>` where you write something like "Register comment for xxx". Use the recipe variable to switch out "xxx" with the recipe title.

Next, we will add a form below our heading. Forms can be a bit tricky, so we have completed a form for you:

```python
<form action="{% url 'cookbook:comment' recipe.id %}" method="post">
    {% csrf_token %}
    <input type="text" name="author" id="author" placeholder="Author">
    <br />
    <textarea name="comment" id="comment" placeholder="Comment"></textarea>
    <br />
    <input type="submit" value="Register">
</form>
```

The _form action_ url specifies which url we will send our request to, and the _method_ specifies that we will make a POST request. `csrf_token` is a Django safety measure to prevent harmful input to compromise our application, but don't worry about this. This is just something we have to add, and then Django will handle the input validation for us. Next, you see a `<input>` of type _text_, and then a `<textarea>`. The different between these two is that `<input>` displays itself as a one liner, while `<textarea>` spans over multiple lines. Finally, we have a `<input>` of type _submit_, which is actually a button that sends the POST request once you click it. The `<br />` tags is just to make some space between the input fields, and you can remove them or add as many as you want.

The submit button will redirect us back to the detail view, but the user might reconsider publishing a comment before submitting. To make it easier to navigate back to the detail view, add a _back_ button like we did in `detail.html`. Remember to use the correct url name and pass `recipe.id` as a parameter.

The final step in this task is to add a link from the detail view (`detail.html`) to the comment view (`comment.html`). You could for instance use a `<p>` with the text "Register a new comment", and then wrap a link around it. Again, remember to use the correct url name and pass `recipe.id` as a parameter.

Reload the page once you are finished with the link. Try to add a new comment in your new comment view, and check if it appears in the detail view. Did it work? Great job! If not, ask an Itera employee for help or check out the `__solutions__` folder.

---

Finished with your task? Click [here](/__tasks__/optional) to go back to the optional tasks.

You can find the solutions for optional task 5 [here](/__solutions__/optional/task5_comments).

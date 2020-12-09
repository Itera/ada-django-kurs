# Task 4: Add new recipe attribute (likes)

Level of difficulty: **medium+**.

In this task, we will add the possibility to _like_ recipes. This could be useful if you are sharing your cookbook with others, and someone wants to try something popular and well-liked. To achieve this, we will add a new attribute to our recipe model: _likes_.

The first thing you will have to do is to create a new field in our `Recipe` model.

Open `models.py` and create a new field called `likes`. The `likes` field will be of type _IntegerField_, and we would like the default value to be zero. Here is an example of how this field could be defined:

```python
[VARIABLE] = models.IntegerField(default=0)
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

The next step is to add the logic for incrementing the likes value. Open `views.py` and insert the following code snippet above the render statement in the `detail` function:

```python
if request.method == "POST":
    recipe.likes += 1
    recipe.save()
```

Remember to switch out `recipe` with the variable name you chose when you retrieved the recipe in part 2.

The code snippet works like this: if the request from the template is a POST request, i.e. that we want to modify something (for instance write to the database), then we increase the recipe's `likes` value by one and save the change to the database. This is all the logic we need to increment the value in the database.

However, we must also make some changes to the template to display and increment the `likes` value. Open `detail.html`, and add a `<p>` tag containing our new `likes` variable, like we have done previously for `description` and `ingredients`. If you are unsure where to place it, you could for instance render it under the recipe title. If you would like to see the number of likes when browsing for recipes as well, you could add the same HTML tag with `recipe.likes` in `index.html`.

Additionally, we need to add a button so that we can increment the `likes` value. To achieve that, we need a simple _form_ containing a button named _Like_. Forms can be a bit tricky, so we have completed a form for you:

```python
<form method="post">
    {% csrf_token %}
    <input type="submit" value="Like">
</form>
```

The _form method_ specifies that we will make a POST request. `csrf_token` is a Django safety measure to prevent harmful input to compromise our application, but don't worry about this. This is just something we have to add, and then Django will handle the input validation for us. Inside the form we have a `<input>` of type _submit_, which is a button that sends the POST request once you click it. This is all we need to trigger the logic we recently wrote in `views.py`.

Head over to the application and open (or reload) a recipe. Did the likes appear? And is it possible to increment the value? Great! If not, check out the `__solutions__` folder or ask an Itera employee for help.

---

Finished with your task? Click [here](/__tasks__/optional) to go back to the optional tasks.

You can find the solutions for optional task 4 [here](/__solutions__/optional/task4_likes).

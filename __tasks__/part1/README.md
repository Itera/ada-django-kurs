# Part 1: Implementing the list view

## Introduction

In this part, you will get to know the main page of our application, `index.html`, where all registered recipes will be listed. You can access this page by typing _/cookbook_ in the address bar.

## Task 1: Retrieve recipes from database

If you open `cookbook/templates/cookbook/index.html` in the code editor, you can see that we have hardcoded a recipe into the page template. However, we have a collection of recipes in our database that we want to render in our web application. Achieving this is the main focus of this task.

Open `cookbook/views.py` in the code editor. This is where the _views_ of our application is defined. Views define what happens when the user opens a certain page in their web browser. In this case, the view `index` renders a static HTML template called `index.html`. We are now going to add some more logic inside the `index` function.

The first step is to retrieve the recipe objects from the database. This can be done using the following syntax, where `[MODEL]` specifies what type of objects we want to retrieve from our database:

```python
item_list = [MODEL].objects.all()
```

In our case, we are interested in the model `Recipe`. This can be achieved by changing the previous command to the following:

```python
recipe_list = Recipe.objects.all()
```

Remember to import the model by putting the following on top of the file:

```python
from .models import Recipe
```

The next step is to render these objects in the static template, called `index.html`. For the template to be able to handle these objects, we have to pass them on as _context_ to the template. Context is an object that are used in the render function, and is just a fancy way of saying that we need to send these objects to the template. You can define a context like this:

```python
context = {"item_list": item_list}
```

To include this context in the render function, you can add it as a third parameter:

```python
return render(request, "cookbook/index.html", context)
```

Define your `recipe_list` variable in the context. Once this is done, you can add it as a third parameter in the render function (behind the `index.html` reference). Save the file, reload the page _/cookbook_ and see what happens.

Did the database objects appear on your screen?

Unfortunately no, the page looks the same as before. Did you understand why? As you might have guessed, we first have to change `index.html` to actually use our dataset. This process is defined in the next task.

## Task 2: Display retrieved objects in index.html

You have now retrieved the database objects, and it's time to render them in our template. We only have one hardcoded recipe in our template, and it's your job to switch out this recipe with our new dataset.

The first step is to for-loop through the dataset. The for-loop can be written as you would usually do in Python, but since this is a HTML file, you have to add some characters around it to declare that this is Python code and not HTML. Here is an example:

```
{% for item in item_list %}
    ** some logic here **
{% endfor %}
```

The items in your for-loop can then be rendered using HTML tags. One easy way to do this is to use a `<p>` tag (paragraph) for each item and render the content inside it. Again, we have to use a special syntax for rendering Python variables in a HTML file. Here is an example:

```html
<p>{{ item }}</p>
```

Your output should now be a list of the recipe objects, where each object has a format like this: `Recipe object (1)`. However, this is not very readable, is it? This is because we print the whole object, which is not very user-friendly. To fix this, we can instead render specific attributes of the object, for instance the `title` of our recipe. To use the attribute `title`, you can use the following syntax:

```html
<h2>{{ item.title }}</h2>
```

Note that we wrapped the recipe title in a HTML `<h2>` tag instead of a `<p>` tag. `<h2>` is a heading tag in HTML, and is the second largest heading one can use.

Did the recipe titles appear on your screen? For-loops and data rendering is a bit tricky in HTML, so check out the `__solutions__` folder if you experience some issues.

## Task 3: Order your dataset

Now we can go ahead and explore our data. But wouldn't it be easier to locate a recipe if they were ordered alphabetically? Or perhaps you want to display the newest recipes on top? No problem! This can easily be achieved by rewriting the object retrieval in `views.py` to the following format:

```python
object_list = [MODEL].objects.order_by("[ATTRIBUTE]")
```

If you would like an alphabetical order, the recipe titles would probably be the most obvious field to order by. Here is how you could do it:

```python
recipe_list = Recipe.objects.order_by("title")
```

If you would like to order the items based on publishing date, you should order by the attribute `pub_date`. Here is an example:

```python
recipe_list = Recipe.objects.order_by("pub_date")
```

However, this command orders the objects ascending, this means that the oldest objects appear on top. You might be more interested in viewing your newest recipes first, right? This is called a descending order, and can be achieved by placing a `-` before your attribute name. Here is an example of the syntax:

```python
recipe_list = Recipe.objects.order_by("-pub_date")
```

Your recipes are now ordered from newest publishing date to the oldest. Choose the ordering that suits you the best, and remember that you can always change this ordering later if you want to.

---

Ready for part 2 of the course? Click [here](/__tasks__/part2) to go to the next tasks.

You can find the solutions for part 1 [here](/__solutions__/part1).

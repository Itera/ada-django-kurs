# Task 2: Add new recipe attribute (duration)

Level of difficulty: **medium**.

If you are in a hurry, wouldn't it be great to see how long time it takes to cook each dish? In this task, we will add a new attribute to our recipe model: _duration_.

The first thing you will have to do is to create a new field in our `Recipe` model.

Open `models.py` and create a new field called `duration`. The `duration` field will be of type _TextField_, so you can take a look at `title`, `description` and `ingredients` and reuse the syntax for those. Be sure to save the file once you have added the `duration` field.

Next, we need to let our database know about the changes to our model. To do this, we create a _migration_, which describes the changes we have made. After we have created the migration, we apply the migration to let the database know about the changes.

First, click on the terminal in repl.it. Type the following into the terminal, and press enter:

```python
python manage.py makemigrations cookbook
```

This command created a migration with the changes you have made. Further, we will apply the migration with the following command:

```python
python manage.py migrate cookbook
```

Type it into your terminal, and press enter. Now you should see a message ending with `OK`. If not, ask an Itera employee for help.

The next step is to add the duration value for a few recipes, such that we can display the duration in our application. To do this, we will use the Django admin panel. This is a page where you, among other things, can see and edit all the content in your database.

Head over to _/admin_, and log in with username _ada_ and password _lovelace_. Navigate to `Recipes`, and then click on a recipe you want to add `duration` to. Fill in a duration value, for instance "30 min", and save the changes. Repeat this a few times such that we have some testdata.

Once you have created the testdata for the `duration` field, open `detail.html`. Add a `<p>` tag containing our new duration variable, like we have done previously for `description` and `ingredients`. If you are unsure where to place it, you could for instance render it under the recipe title or under the description title. Note that for the recipes that do _not_ have the `duration` field, Django will just render an empty `<p>` tag. If you would like to see the duration value when browsing for recipes, you could repeat these steps in `index.html` as well.

Save the file, and head over to one of your modified recipes in the application. Did the duration value appear? Great! If not, check out the `__solutions__` folder or ask an Itera employee for help.

---

Finished with your task? Click [here](/__tasks__/optional) to go back to the optional tasks.

You can find the solutions for optional task 2 [here](/__solutions__/optional/task2_duration).

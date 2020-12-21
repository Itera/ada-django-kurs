# Task 1: Add new recipe attribute (author)

Level of difficulty: **medium**.

Many students live in a shared house, and you might want to share your cookbook with the rest of the household. Perhaps the other habitants want to contribute to the cookbook as well? In that case, it could be useful to gather information regarding who has written this recipe. To solve this, we will add a new attribute to our recipe model: _author_.

The first thing you will have to do is to create a new field in our `Recipe` model.

Open `models.py` and create a new field called `author`. The `author` field will be of type _TextField_, so you can take a look at `title`, `description` and `ingredients` and reuse the syntax for those. Be sure to save the file once you have added the `author` field.

Next, we need to let our database know about the changes to our model. To do this, we create a _migration_, which describes the changes we have made. After we have created the migration, we apply the migration to let the database know about the changes.

<!-- Sjekk ut hvordan dette gjøres i repl.it -->

First, open the terminal in repl.it. Type the following into the terminal, and press enter:

```python
python manage.py makemigrations cookbook
```

This command created a migration with the changes you have made. Further, we will apply the migration with the following command:

```python
python manage.py migrate cookbook
```

Type it into your terminal, and press enter. Now you should see a message ending with `OK`. If not, ask an Itera employee for help.

The next step is to add the authors for a few recipes, such that we can display the authors in our application. To do this, we will use the Django admin panel. This is a page where you, among other things, can see and edit all the content in your database.

Head over to _/admin_, and log in with username _XXX_ and password _YYY_. Navigate to `Recipes`, and then click on a recipe you want to add authors to. Fill in a value for `author`, for instance "Ada Lovelace", and save the changes. Repeat this a few times such that we have some testdata.

Once you have created the testdata for the `author` field, open `detail.html`. Add a `<p>` tag containing our new author variable, like we have done previously for `description` and `ingredients`. If you are unsure where to place it, you could for instance render it under the recipe title. Note that for the recipes that do _not_ have the `author` field, Django will just render an empty `<p>` tag. If you would like to see the author when browsing for recipes, you could repeat these steps in `index.html` as well.

Save the file, and head over to one of your modified recipes in the application. Did the author appear? Great! If not, check out the `__solutions__` folder or ask an Itera employee for help.

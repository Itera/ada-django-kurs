# Part 3: Styling the application

## Introduction

In this part, we will give our application a more finished touch. Follow the tasks below, and then explore Django, HTML and CSS through the optional tasks. You can find these in the `__tasks__` folder.

## Task 1: Add link to each recipe

To make it easier to explore different recipes, we want to make the recipe titles clickable and link to the recipe detail page. A link can be defined like this:

```html
<a href="[PATH]">Lorem impsum</a>
```

`[PATH]` is the URL we want to navigate to, and one could for instance specify www.vg.no here. However, we want to navigate to another page within our application, and the `recipe_id` plays an important role here. How to pass this on dynamically?

Open `cookbook/urls.py` and take a look at the code. First, you see that the `app_name` is set to _cookbook_. Further, you can see a variable `urlpattern` containing several paths. The paths are built with the following structure:

```python
path("[URLPATH]", [VIEW], [NAME])
```

To refer to such paths from other files, you can use the following syntax:

```python
"{% url '[APP_NAME]:[NAME]' %}"
```

With this command, Django does a little magic for you, and renders the view associated with `'[APP_NAME]:[NAME]'`. However, for the detail view path, we also need the parameter `recipe_id`. To pass such variables into the URL path, you can add it as a parameter. Django will then use this variable in the path. Here is an example:

```python
"{% url '[APP_NAME]:[NAME]' [VARIABLE] %}"
```

Open `index.html`, and combine the HTML `<a>` tag and the Django URL to create a link to each recipe. You can solve this by adding the `<a>` tag around the recipe title.

Did you manage to create the link? If not, don't worry! Check out the `__solutions__` folder for an example of how you might do it.

## Task 2: Add back button in the detail view

Now it's easy to navigate to a specific recipe, but we should also make it easier to navgiate back to the recipe list in case we want to explore other recipes. To achieve this, we will add a _back_ button in the detail view. This can be performed in the same way as in the previous task, except this time we do not need to include a variable in the URL path.

Open `detail.html` and include an HTML `<p>` tag with the text _Back_ inside it. Try adding a link around it. Remember that `[APPNAME]` will stay the same, but you have to switch out `[NAME]` with the correct URL name.

Did it work? Great! If not, ask an Itera employee for help or check out the `__solutions__` folder.

Good job! Now it's much easier to navigate and use the application the way it is supposed to.

## Task 3: Add images in the list view

To make the list view a bit more appealing, we will display the images here like we did in the detail view. To achieve this, you can reuse the for-loop you wrote in part 1 and add an HTML `<img>` tag inside it. Here is a short recap of you images can be rendered:

```
<img src={{ [VARIABLE].image.url }} width="500px" />
```

Once you have added the tag, reload the list page. Now you can see the images for each recipe, in addition to the titles you rendered in part 1. Great job!

## Task 4: Styling the recipes in the list view

To make our list view more neat, we want a grid based view where the recipes are displayed beside each other. To achieve this, we will use a CSS layout model called _Flexbox_. The Flexbox styling is already fixed for you in `style.css`, which can be found under `static/cookbook`, so the only thing you will have to do is use the following class names in your HTML structure:

- `recipe-list`: styling for a `<div>` containing the recipes
- `recipe-list-item`: styling for a `<div>` containing one recipe
- `recipe-image`: styling for an `<img>` containing the recipe image

To use these class names, the HTML can be structured like this:

```html
<div class="<containername>">
  *your for-loop starts here*
  <div class="<itemname>">
    <img src="..." class="<imagename>" />
    *your recipe title goes here*
  </div>
  *your for-loop ends here*
</div>
```

Try to recreate this structure in `index.html`, while still preserving the code from earlier steps. Reload the page, and you will see a grid based view of your recipes. If you resize your window size, the recipes will move accordingly. Remember to remove the `width` property from the `<img>` tag if you haven't already.

Is it not working properly? Remember to ask an Itera employee for help or check out the `__solutions__` folder.

Open `style.css` and read the styling defined for `recipe-list`, `recipe-list-item` and `recipe-image`. Do you understand what each CSS property does?

We have defined a few tasks in `style.css`:

- `recipe-list`: change flex direction to _column_ instead of _row_
- `recipe-list-item`: change flex-direction to _row_ instead of _column_
- `recipe-image`: change width from _300px_ to _150px_

Follow the tasks and reload the page. Did you notice what happened?

:exclamation: If the style still looks the same, you should try a hard refresh in the browser. A hard refresh can be performed by using `cmd + shift + R` on Mac or `ctrl + shift + R` on Windows.

Your page is now built like this:

- Recipes are listed column-wise, i.e. vertically instead of horizontally.
- Recipe details (images and titles) are displayed row-wise, i.e. horizontally instead of vertically.
- Recipe images are more narrow (150 pixels instead of 300 pixels).

Note that this was just a quick experiment, so be sure to revert these changes before continuing. Having said that, feel free to explore with the margins and width defined for `recipe-list-item`.

## Task 5: Styling the recipe in the detail view

Last, but not least, we need to style the detail view. Like we did with the list view, we have also defined CSS you can use in your detail template. Here is the class names and how they should be used:

- `recipe-details`: styling for a `<div>` containing the ingredients and the description
- `recipe-ingredients`: styling for a `<div>` containing the ingredients
- `recipe-description`: styling for a `<div>` containing the description

```html
*image and title goes here*
<div class="<containername>">
  <div class="<name1>">*name1 content goes here*</div>
  <div class="<name2>">*name2 content goes here*</div>
</div>
```

Try to recreate this structure in `detail.html`, while still preserving the code from earlier steps. The styling in `style.css` assumes that the ingredients `<div>` comes before the description `<div>`, so we recommend you to place them in that order. Reload the page and see how your page components have moved.

Open `style.css` and read the styling defined for `recipe-details`, `recipe-ingredients` and `recipe-description`. Do you understand what each CSS property does?

We have defined a couple of tasks in `style.css`:

- Add styling to `recipe-ingredients`
- Add styling to `recipe-description`

How you want to style the detail page is completely up to you, but if you are out of ideas, you can check out the following properties:

- background-color: https://www.w3schools.com/cssref/pr_background-color.asp
- text-align: https://www.w3schools.com/cssref/pr_text_text-align.asp
- border-style, border-width and border-color: https://www.w3schools.com/cssref/pr_border-style.asp
- text-decoration: https://www.w3schools.com/cssref/pr_text_text-decoration.asp

---

After some CSS exploring, head over to the [optional tasks](/__tasks__/optional) and see if there is something you would like to learn more about. You can also continue playing with CSS and all the properties that it has, if you find that more interesting. Maybe you have a design idea, but are uncertain of how you can implement it? Ask an Itera employee for help, and we will figure it out together :smile:

You can find the solutions for part 3 [here](/__solutions__/part3).

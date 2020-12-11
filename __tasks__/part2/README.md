# Part 2: Implementing the detail view

## Introduction

In this part, you will get to know the detail page, where one single recipe is displayed. This page is called `detail.html`, and you can access it by typing _/cookbook/<id>_ in the address bar.

## Task 1: Retrieve recipe from database

Open `views.py` in the code editor. As you can see, the view `detail` renders a static HTML template called `detail.html`, and it takes `recipe_id` as a parameter. `recipe_id` is a unique identifier for a recipe, and we are going to use this value to retrieve the correct recipe.

Retrieving an objects based on its identifier, also called _primary key_ or _pk_, can be achieved by using the following expression:

```python
item = [MODEL].objects.get(pk=[ID])
```

This command will retrieve the object that matches the given id. However, if we try a primary key that does not exist, the server will send a HTTP response that the item could not be found, and our application will crash. Fortunately, Django has a clever way of handling such an error, where the user receives a warning without having the application to crash. This function is called `get_object_or_404`, and handles both the retrieval of the object and error handling if the object does not exist. Here is an example of how it can be used:

```python
item = get_object_or_404([MODEL], pk=[ID])
```

Copy this function to your detail view, import `get_object_or_404` from `django.shortcuts` and switch out `[MODEL]` and `[ID]` with the correct model and identifier. Pass the item on as context to the render function, like we did in the previous part. Once you have completed this, go on to the next task where we will use this retrieved recipe and render it in our application.

Are you uncertain on how to implement the 404-handling, or are you experiencing any issues? Ask an Itera employee for help or check out the `__solutions__` folder.

# Task 2: Display retrieved object in detail.html

In the previous task you passed the recipe on to the template as context, and now it's time to render this object in our template. This is very similar to task 2 in the previous part, so here is a short recap of how you could render your recipe:

```html
<p>{{ item }}</p>
```

Remember that you can also render specific attributes, for instance `title`, with the following syntax:

```python
item.title
```

Once you have rendered a variable or two, take a look at _cookbook/1_. Did the recipe information appear in your application? If yes, great! If no, take a look at the `__solutions__` folder and see if there is something missing.

Once the rendering is in order, you can explore different types of HTML elements and build the detail page the way you want. You could for instance use `<h1>` for the recipe title, `<h2>` as headings for ingredients and description, and `<p>` for rendering of the retrieved ingredients and descriptions.

You might have noticed that the description and ingredients looks a bit strange when rendering them? That's because we have created those elements with linebreaks, but Django does not render these linebreaks by default. To allow linebreaks in a variable to be rendered, you can use the following syntax:

```html
<p>{{ variable | linebreaks }}</p>
```

# Task 3: Display recipe image in detail.html

In addition to titles, descriptions and ingredients, we have also stored an image for each recipe. These images are located in the subfolder `recipe` within the `media` folder.

Images can be rendered using an image-specific HTML tag called `<img>`. The `<img>` tag has a parameter called `src`, which specifies which path Django can use to find the image source. The `<img>` tag can be used like this:

```html
<img src="[PATH]" />
```

As mentioned above, the image collection is stored in the `media` folder. For Django to find this image collection, we must first specify where Django might find such media content.

Open `djangokurs/settings.py` and add these two lines at the bottom of the file:

```python
MEDIA_ROOT = "media"
MEDIA_URL = "/media/"
```

These two lines specify that Django should look for images in the `media` folder, where our application has a subfolder `recipe` containing our images. However, Django knows to look within this folder since the name of the folder matches the model name.

Now it's time to render our image, so go ahead and open `detail.html`. Since we have now declared where Django might find our pictures, you can specify the path like this:

```
<img src={{ [VARIABLE].image.url }} />
```

Copy this command and switch out `[VARIABLE]` with your own recipe variable. Reload the page. Did it appear? Great! However, the picture is quite big. This can easily be solved by adding a `width` property to the HTML tag:

```
<img src={{ [VARIABLE].image.url }} width="500px" />
```

In this case, the `width` property is set to 500 pixels wide. Explore different sizes and find the one you like.

# Web development with Django

Welcome to our web development course in Django! This course will give you an introduction to Django and its core concepts, in addition to learning how HTML and CSS can be used to form a simple web page.

## How to start the application

To avoid problems with wrong Python versions and dependency issues, we will use an online code editor called repl.it. Repl.it is perfect for short courses like this, as you can just import the code to this online editor instead of setting everything up on your personal laptops.

1. Head over to repl.it and create your own account.
2. Click on the button `New repl`, and choose the tab `Import from GitHub`. Import this repository by copying and pasting the following link: https://github.com/Itera/ada-django-kurs

Wait for repl.it to complete the import. The import is finished once you are able to type in the different files.

Our project is now imported, and it is almost time to get started! However, there is a few things we have to do first.

Click on the terminal in the bottom right corner (the dark box), and press enter to get a new line. We now have to install the requirements for our project. Type this into your terminal and press enter:

```
pip install -r requirements.txt
```

The command is finished once you get a new command line you can type into. Hopefully, you can see something like "Successfully installed Django..." on the bottom of the terminal screen. If you receive warning about pip version, you can just ignore it.

Press the `Run` button on the top of your repl.it page. Now your application is running! The application preview on the right is quite small, so we recommend you to open the application in a new tab. To do this, click on the squared button with a arrow inside it. Note that this might take a while. If you would like, you can now close the application preview on the right.

Before starting on the tasks in the `__tasks__` folder, read the project introduction below to get an overview of how the application is built and how your data is structured.

## Project overview

### How is our application structured?

The project we are going to be working with today is a collection of recipes. To provide you some recipes in the application, we have created a database in advance. Please note that the recipes are just examples, so exploration of these are at your own risk ;)

#### List view

Open the url https://ada-django-kurs.[REPLIT_USERNAME].repl.co/cookbook/. This is our **list view**, where all our recipes will be displayed. For now we have "hardcoded" a recipe to show you some content, but one of your first tasks will be to retrieve and display the recipes here.

#### Detail view

Open the url https://ada-django-kurs.[REPLIT_USERNAME].repl.co/cookbook/1. This is our **detail view**, where the specifics of a single recipe will be displayed. The _1_ in the url indicates that we are looking at the recipe with _id = 1_. To show you some content, we have hardcoded a recipe here also. Displaying a recipe and its details will be one of your later tasks.

#### Admin view

Open the url https://ada-django-kurs.[REPLIT_USERNAME].repl.co/admin and log in with the username _XXX_ and password _YYY_. Now you are in the **admin view** of our application. Click on the link `Recipes`, and you will see a list of all the recipes we have registered in the database. These are the recipes you are going to retrieve and display in our application. If you are curious, you can also click on each recipe and view and edit its specifics.

### How does Django work?

For this project, the following files are relevant to take a look at:

- `index.html`
- `detail.html`
- `style.css`
- `views.py`
- `urls.py`
- `models.py`

![Diagram of the different django files.](media/django.png)

`urls.py` defines which pages we can access through our application, for instance _/cookbook_ and _/cookbook/1_, and associates these with _views_. The views are defined in `views.py`, and decides what content or which templates to render for the different views.

`index.html` and `detail.html` are static templates, and are written in HTML. The templates define what type of content the web page should contain, and the content is styled using the CSS in `style.css`. These three files construct the "visual" part of our web application.

For a description of `models.py`, take a look at the section below.

### How is our data structured?

The database models is defined in `models.py`, and specifies what kind of objects we would like to store, in addition to which attributes (_fields_) are associated with them. For instance, our recipe model have the following fields:

- title
- description
- ingredients
- image
- pub_date (date published)

The first three fields are of type `TextField`, and stores textual input. Image is of type `ImageField`, and stores images, as you might have guessed. Pub-date is of type `DatetimeField`, and stores a timestamp. We have configured that the default value for this field is the current timestamp, if the field value is not specified by the user.

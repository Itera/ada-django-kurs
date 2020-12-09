# Web development with Django :rocket:

Welcome to our web development course in Django! This course will give you an introduction to Django and its core concepts, in addition to how HTML and CSS can be used to form a simple web page :computer:

## How to start the application

To simplify the process of setting up the project, we will use an online code editor called repl.it. Repl.it is perfect for short courses like this, as you can just import the code to this online editor instead of setting everything up on your personal laptops.

1. Head over to [repl.it](https://repl.it) and create your own account.
2. Click on the button `New repl`, and choose the tab `Import from GitHub`. Import this repository by copying and pasting the following link: https://github.com/Itera/ada-django-kurs. The import view looks like this:

<img src="media/replit-import.png" alt="Illustration of the repl.it import." width="50%" />

3. Wait for repl.it to complete the import. If you receive an error saying that "The IDE is having a bit of trouble", click the `Reload` button as suggested by repl.it. The import is finished once you see the file tree and code editor, as shown in the screenshot below.

<img src="media/replit-view.png" alt="Illustration of the repl.it editor." />

Our project is now imported, and it is almost time to get started!

Press the `Run` button on the top of your repl.it page. Repl.it will now install all the packages that are required to run your application. Once a window with the title "My recipe list" opens, the application has started successfully :tada:

The application preview on the right is quite small, so we recommend you to open the application in a new tab. To do this, click on the squared button with an arrow inside it. Your application will now open in a new tab in your browser.

Before starting on the tasks in the `__tasks__` folder, read the project introduction below to get an overview of how the application and the database are structured.

## Project overview

### How is our application structured?

The project we are going to be working with today is a collection of recipes :pizza: To provide you some recipes in the application, we have created a database in advance. Please note that the recipes are just examples, so exploration of these are at your own risk :smile:

#### List view

Open the url https://ada-django-kurs.[REPLIT_USERNAME].repl.co/cookbook/. This is our **list view**, where all our recipes will be displayed. For now we have "hardcoded" a recipe to show you some content, but one of your first tasks will be to retrieve and display the recipes here.

#### Detail view

Open the url https://ada-django-kurs.[REPLIT_USERNAME].repl.co/cookbook/1. This is our **detail view**, where the specifics of a single recipe will be displayed. The _1_ in the url indicates that we are looking at the recipe with _id = 1_. To show you some content, we have hardcoded a recipe here as well. Displaying a recipe and its details will be one of your later tasks.

#### Admin view

Open the url https://ada-django-kurs.[REPLIT_USERNAME].repl.co/admin and log in with the username _ada_ and password _lovelace_. Now you are in the **admin view** of our application. Click on the link `Recipes`, and you will see a list of all the recipes we have registered in the database. These are the recipes you are going to retrieve and display in our application. If you are curious, you can also click on each recipe and view and edit its specifics.

### How does Django work?

For this project, the following files are relevant to take a look at:

- `cookbook/templates/cookbook/index.html`
- `cookbook/templates/cookbook/detail.html`
- `cookbook/static/cookbook/style.css`
- `cookbook/views.py`
- `cookbook/urls.py`
- `cookbook/models.py`

<img src="media/django.png" alt="Diagram of the different django files." width="50%" />

`urls.py` defines which pages we can access through our application, for instance _/cookbook_ and _/cookbook/1_, and associates these with _views_. The views are defined in `views.py`, and decides what content or which templates to render for the different views.

`index.html` and `detail.html` are templates written in HTML. The templates define what type of content the web page should contain, and the content is styled using the CSS in `style.css`. These three files construct the "visual" part of our web application.

For a description of `models.py`, take a look at the section below.

### How is our data structured?

The database models are defined in `models.py`. The file specifies what kind of objects we would like to store, in addition to which attributes (_fields_) are associated with them. For instance, our recipe model has the following fields:

- title
- description
- ingredients
- image
- pub_date (date published)

The first three fields are of type `TextField`, and store textual input. Image is of type `ImageField`, and stores an image, as you might have guessed. Pub-date is of type `DatetimeField`, and stores a value for a specific point in time. We have configured that the default value for this field is the current timestamp, if the field value is not specified by the user.

### Tasks and solutions

Now it's time to get started on the tasks! :raised_hands: The `__tasks__` folder is structured like this:

- `part1`: tasks for part 1 of the course.
- `part2`: tasks for part 2 of the course.
- `part3`: tasks for part 3 of the course.
- `optional`: tasks you can explore if you are finished with the tasks ahead of time, or would like to challenge yourself after the course is finished.

Click [here](/__tasks__/part1) to go to the tasks for part 1 of the course.

Note that we also have a `__solutions__` folder with the same structure as `__tasks__`, where you can find complete solution proposals for the different tasks. Click [here](/__solutions__) to go to the `__solutions__` folder. However, we recommend you to ask an Itera employee for help if you are stuck at a task :smile:

## Troubleshooting

### The site doesn't load (issue #1)

You might experience that your repl.it project stops due to inactivity or by an accident. If your application is running properly, you should see a button named `Stop` on the top of your repl.it page. Otherwise, press the `Run` button on the top of your repl.it page to restart your application.

If try to press `Run` and the application still won't start, have a look in the console (black window on the right). Does it give you any errors? If it does and you cannot figure out why, reach our to one of the employees from Itera and we will help you.

### The site doesn't load (issue #2)

If you are using a Mac with operating system Big Sur, you might experience DNS issues. To keep a long story short: the browser struggles to find the website's location on the internet. This can be solved by adding Google's DNS server:

1. Go to `System preferences` on your Mac.
2. Choose `Network`, and click on `Advanced`.
3. Click the `DNS` tab, and you will see a list to the left with the name `DNS servers`.
4. Click the `+` sign and add `8.8.8.8` to your list of DNS servers. Remember to click `OK` and then `Apply` when you are done.

Reload the page. Hopefully, your application will appear :smile:

### Getting a certificate error when opening in a new tab

Some might experience warnings like "Your connection is not private" or "This site is not secure" when opening the application in a new tab. This is a security measure browsers have to prevent you from accessing pages where the network traffic is not encrypted. If this warning had been for a serious web site, you should be careful to proceed to the page. Our page, however, is just a testing application with no sensitive information, so we can ignore this warning.

Here's the most common ways to override such certificate errors:

- **Chrome**: press the `Advanced` button, and then choose `Proceed to [LINK] (unsafe)`.
- **Safari**: press the `Show Details` button, and then click the `Visit website` from the pop up.

Unfortunately, **Firefox** does not provide an easy way for overriding the certificate warning and proceeding to the page. If you are using Firefox and experiencing this issue, you should test your application with another browser.

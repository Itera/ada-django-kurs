# Task 1: Add preview of recipe description in list view

Level of difficulty: **easy**.

To make the list view more appealing, we want to add a preview of the recipe description as well.

The first step is to render the description attribute underneath the recipe title. You could for instance use the `<p>` tag for this purpose. Open `index.html` and add the recipe description where it belongs. Once you have added the description, save the file and reload the page. Hopefully, the recipe descriptions will appear in your application.

However, the description is often quite long, and we are not interested in seeing the full content. Therefore, we would like to crop the text to 100 characters, such that the preview of each recipe becomes much smaller. Cropping a text in Django can be achieved like this:

```html
<p>{{ [ATTRIBUTE] | slice:"0:100" }}</p>
```

Try adding this to your recipe description. Did it work? Great! If not, ask an Itera employee for help or check out the optional tasks in the `__solutions__` folder.

from datetime import datetime

from django.db import models


class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to="recipes")
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

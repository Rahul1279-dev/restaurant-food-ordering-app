from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    ("starters", "Starters"),
    ("drinks", "Drinks"),
    ("main_course", "Main Course"),
    ("seafood", "Seafood"),
    ("burgers_and_sandwiches", "Burgers and Sandwiches"),
    ("deserts", "Deserts"),
    ("beverages", "Beverages"),
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available"),
)

class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal

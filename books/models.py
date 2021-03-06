from django.db import models

# Create your models here.

# we want to have a Book table inside our database


class Book(models.Model):
    # what are the fields (aka attributes) of this table

    # eqv. title VARCHAR(255) NOT NULL
    title = models.CharField(blank=False, max_length=255)

    # eqv. ISBN VARCHAR(255) NOT NULL
    ISBN = models.CharField(blank=False, max_length=255)

    # eqv. desc TEXT NOT NULL
    desc = models.TextField(blank=False)

    # toString function -- it allows us to state the string representation
    # of a class
    def __str__(self):
        return self.title


class Publisher(models.Model):
    # the fields (aka attributes) of the table
    name = models.CharField(blank=False, max_length=100)
    email = models.CharField(blank=False, max_length=100)
    website = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

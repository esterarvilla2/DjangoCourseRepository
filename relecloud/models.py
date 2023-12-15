from django.db import models
from django.urls import reverse

# Create your models here.
# In this script we want to put in our database.
# Description of the tables, properties
# Models -> tables
# Fields -> columns

class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,  # larger than a CharField
        null=False,
        blank=False
    )
    slug = models.SlugField()
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('destination_detail', kwargs = {'pk': self.pk})

class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,  # larger than a CharField
        null=False,
        blank=False
    )
    destinations = models.ManyToManyField(
        Destination, 
        related_name = 'destinations'
    )
    def __str__(self) -> str:
        return self.name

class InfoRequest(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    email = models.EmailField()
    notes = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    cruise = models.ForeignKey(
        Cruise,
        on_delete=models.PROTECT
    )

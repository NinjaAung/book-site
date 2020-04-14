import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

# python manage.py shell


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Book(models.Model):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    date_published = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    # def was_published_recently(self):
    #     return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title


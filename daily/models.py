from django.db import models
from markdownx.models import MarkdownxField
import datetime


class Daily(models.Model):
    date = models.DateField()
    univ = MarkdownxField()
    study = MarkdownxField()
    other = MarkdownxField()
    first_meet = MarkdownxField()
    wanna_do = MarkdownxField()
    summary = MarkdownxField()
    evaluation = models.ForeignKey('Evaluation', on_delete=models.PROTECT)
    isOpen = models.BooleanField(default=True)

    def __str__(self):
        date_str = self.date.strftime('%Y/%m/%d')
        return date_str


class Evaluation(models.Model):
    evaluation = models.CharField(max_length=255)

    def __str__(self):
        return self.evaluation


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    twitter = models.CharField(max_length=50)
    oshi = models.CharField(blank=True, max_length=50)
    content = models.TextField()
    datetime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name

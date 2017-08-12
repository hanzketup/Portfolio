# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cat(models.Model):
    title = models.TextField()
    color = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):

    title = models.CharField(max_length=150)
    date = models.DateField()

    short = models.TextField()

    content = tinymce_models.HTMLField()

    cat = models.ManyToManyField(Cat)

    def __str__(self):
        return self.title

class Pro(models.Model):

    title = models.CharField(max_length=150)
    img = models.CharField(max_length=500)

    isexp = models.BooleanField()

    link = models.CharField(max_length=500, blank=True)
    art = models.CharField(max_length=500, blank=True,)

    desc = models.TextField()

    def __str__(self):
        return self.title

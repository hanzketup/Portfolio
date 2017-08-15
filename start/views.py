# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from talk.models import Post, Pro

def index(request):

    posts = Post.objects.all()
    pros = Pro.objects.all()


    snd = {

    "posts":posts,
    "pros":pros,

    }

    return render(request, 'start/index.html', snd)

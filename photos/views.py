# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
import random

def getcat():
    r = Cat.objects.all()
    r = list(r)
    return r

def getimg(request):

    req = requests.get("https://api.imgur.com/3/album/CkXDK/images", headers={"authorization":"Client-ID 8820eceaafeee84"})
    reqd = req.json()['data']

    reqr = random.shuffle(reqd)

    imgs = []

    for i in reqd:
        li = i["link"]
        lim = li[:-4] + 'm' + li[-4:] #imgur thumbnail extract
        imgs.append('<img src="{}" class="pho" data-link="{}" />'.format(lim, li))


    snd = {

        "title":"Photos",
        "title_desc":"Here you'll find a selection of my photos. Click on an image to get a better look!",
        "imgs": imgs,
        "allcat": getcat(),

    }

    return render(request,'photos/list-photos.html', snd)
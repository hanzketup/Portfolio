# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from . import models

admin.site.register(models.Post)
admin.site.register(models.Cat)
admin.site.register(models.Pro)
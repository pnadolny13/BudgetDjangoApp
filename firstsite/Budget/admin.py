# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  Expense, Input, UserInput, UserCategories
# Register your models here.

admin.site.register(Expense)
admin.site.register(Input)
admin.site.register(UserInput)
admin.site.register(UserCategories)


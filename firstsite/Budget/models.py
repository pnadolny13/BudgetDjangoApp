# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_pandas.managers import DataFrameManager

class Expense(models.Model):
    category = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
# this makes it show as a value instead of a object    
    def __str__(self):
        return self.description + ': ' + str(self.date)
    
class Input(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    files_type =models.CharField(max_length=20)
    input_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default = False)
    def __str__(self):
        return self.expense + ' : ' + self.input_title + self.files_type


class UserInput(models.Model):
    user = models.CharField(max_length=20, verbose_name = 'User')
    date = models.DateField(verbose_name = 'Date')
    amount = models.DecimalField(decimal_places=2, max_digits=6, verbose_name = 'Amount')
    category = models.CharField(max_length=50, verbose_name = 'Category')
    expenseLabel = models.CharField(max_length=50, verbose_name= 'Expense Label')
    comment = models.CharField(max_length=100, blank=True, verbose_name = 'Comment')
    objects = models.Manager()
    pdobjects = DataFrameManager()

class UserCategories(models.Model):
    user = models.CharField(max_length=20, verbose_name = 'User')
    category = models.CharField(max_length=50, verbose_name = 'Category')
    objects = models.Manager()
    def __str__(self):
        return self.category
# -*- coding: utf-8 -*-

from django import forms

class ExpenseForm(forms.Form):
    label = forms.CharField(label='Expense Label', max_length=50)
    date = forms.DateField(label='Expense Date')
    amount = forms.DecimalField(label='Amount $', decimal_places=2, max_digits=6)
    category = forms.CharField(label='Category', max_length=50)
    comment = forms.CharField(label='Comment', max_length=100, required=False)
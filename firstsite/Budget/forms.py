# -*- coding: utf-8 -*-

from django import forms
from .models import UserCategories

class ExpenseForm(forms.Form):
        label = forms.CharField(label='Expense Label', max_length=50)
        date = forms.DateField(label='Expense Date')
        amount = forms.DecimalField(label='Amount $', decimal_places=2, max_digits=6)
        category = forms.ModelChoiceField(queryset = UserCategories.objects.filter(user="admin"), label='Category', to_field_name="category")  
        comment = forms.CharField(label='Comment', max_length=100, required=False)

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')
            super(ExpenseForm, self).__init__(*args, **kwargs)
            self.fields["category"].queryset = UserCategories.objects.filter(user__in=[user, "admin"])

class MonthListForm(forms.Form):
        month= forms.CharField(label='Analyze other month?', widget=forms.Select(choices=[ ('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'),('11', 'November'), ('12', 'December')]))
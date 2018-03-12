# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from django_pandas.managers import DataFrameManager
import pandas

import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from .forms import ExpenseForm, MonthListForm
from .models import UserInput, UserCategories
from django_tables2 import RequestConfig
from .tables import UserInputTable


    ##################   NEW     ####################

def index(request):
   return render(request, 'Budget/index.html')

def track(request):
    if request.method == 'POST':
        # validate form first
        form = ExpenseForm(request.POST, user = request.user)
        today = datetime.date.today()
        if form.is_valid():
           label = request.POST.get('label')
           inputDate = request.POST.get('date')
           amount = request.POST.get('amount')
           category = request.POST.get('category')
           comment = request.POST.get('comment')
           entry = UserInput(user= request.user.username, date=inputDate, amount=amount, category=category, expenseLabel=label, comment=comment)
           entry.save()
           return redirect('/budget/track')
        else:
            # this doesnt load a form it just says failed
            return render(request, 'Budget/track.html', {'notification': "Failed to Track"}, {'form': ExpenseForm(user = request.user, initial={ 'date': today, 'comment': 'optional'})})
    elif request.user.is_authenticated:
        # get user name
        currentUser = request.user.username
        
        # get first day of current month
        today = datetime.date.today()
        month= today.replace(day=1)

        # get 10 entries
        qs = UserInputTable(UserInput.objects.order_by("-date").filter(user=currentUser).filter(date__gte=month))
     
        # to allow for sorting 
        # RequestConfig(request).configure(qs)

        form = ExpenseForm(user = request.user, initial={ 'date': today, 'comment': 'optional'})
        return render(request, 'Budget/track.html', {'qs': qs, 'form': form})

    else:
        # you shouldnt have gotten this far without login but check anyways
        return redirect('accounts/login')

def analyze(request):
    # I will show all categories by user plus tax and pay
    # with monthly saved budget settings
    today = datetime.date.today()
    month= today.replace(day=1)
    if request.method == 'POST':
        # validate form first
        form = MonthListForm(request.POST)
        today = datetime.date.today()
        if form.is_valid():
            selected_month = request.POST.get('month')
            month = month.replace(month=int(selected_month))
    
    currentUser = request.user.username
    cats = UserCategories.objects.filter(user=currentUser)
    if currentUser != "admin":
        cats += UserCategories.objects.filter(user="admin")
    
    # get sum of amounts this month, in each category, then add to list

    totals_dict = {}
    total = UserInput.objects.filter(user=currentUser).filter(date__gte=month).filter(category='Income').aggregate(Sum('amount'))
    total_income = str(total['amount__sum'])
    total_spent = 0
    for category in cats:
        cat_sum = UserInput.objects.filter(user=currentUser).filter(date__gte=month).filter(category=category).aggregate(Sum('amount'))

        value = cat_sum['amount__sum']
        # if no data for that category then we cant give data
        if value is None:
            value = 0
            percent = 0
        # if income is empty then we cant give a percentage
        elif total['amount__sum'] is None:
            value = 0
            percent = 0
        else:
            percent = str(round((100 * float(value)/float(total_income)),0))
        # dont include income
        if str(category) == 'Income':
            continue
        totals_dict[str(category)] = [("$ " + str(value)), (str(percent) + "%")]
        total_spent += value

    # then they can play with those numbers percent or dollar amount
    # see monthly flow and save budget settings

    # then we will have same setup with monthly total percentages so far and remaining balance
    # allow them to put in expected additional amounts

    # view by category like my excel sheet monthly - adjust date range

    # weekly budgets, color by how well you did, then click in to see all details
    savings = float(total_income) - float(total_spent)
    save_percent = str(round((100 * float(savings)/float(total_income)),0))
    return render(request, 'Budget/analyze.html', {'totals_dict': totals_dict, 'form' : MonthListForm(initial={ 'month': today.month}), 'income': ('$ ' + total_income), 'savings': ('$ ' + str(savings)), 'save_percent': (str(save_percent) + '%')})

def action(request):
   return render(request, 'Budget/action.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
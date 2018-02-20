# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ExpenseForm

    ##################   NEW     ####################

def index(request):
   return render(request, 'Budget/index.html')

def track(request):
    if request.method == 'POST':
        # validate form first
        form = ExpenseForm(request.POST);
        if form.is_valid():
            label = request.POST.get('label')
            print("label: " + str(label))
            return redirect('/budget/track')
        else:
            # this doesnt load a form it just says failed
            return render(request, 'Budget/track.html', {'notification': "Failed to Track"}, {'form': ExpenseForm()})
    elif request.user.is_authenticated:
        # you shouldnt have gotten this far without login but check anyways
        return render(request, 'Budget/track.html', {'form': ExpenseForm()})
    else:
        return redirect('accounts/login')

def analyze(request):
   return render(request, 'Budget/analyze.html')

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
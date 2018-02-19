# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

    ##################   NEW     ####################

def index(request):
   return render(request, 'Budget/index.html')

def track(request):
    if request.user.is_authenticated:
        return render(request, 'Budget/track.html')
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
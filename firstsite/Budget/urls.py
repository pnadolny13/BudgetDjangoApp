from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Budget'

urlpatterns = [

    ##################   NEW     ####################
    #/budget/
    url(r'^$', views.index, name='index'),
    
    # /budget/track
    url(r'^track$', views.track, name='track'),
    
    # /budget/analyze
    url(r'^analyze$', views.analyze, name='analyze'),
    
    # /budget/take-action
    url(r'^action$', views.action, name='action'),    
    
    #Add Django site authentication urls (for login, logout, password management)
    url(r'^accounts/login/', auth_views.login, name='login'),
    url(r'^accounts/logout/', auth_views.logout, name='logout'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
]



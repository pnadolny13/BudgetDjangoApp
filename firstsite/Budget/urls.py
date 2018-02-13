from django.conf.urls import url
from . import views

app_name = 'Budget'

urlpatterns = [
        
    ################   LEGACY    #################    
    #/budget/
#    url(r'^$', views.index, name='index'),
#    # /budget/<budget.id>/
#    url(r'^(?P<budget_id>[0-9]+)/$', views.detail, name='detail'),
#    # /budget/June/
#    url(r'^(?P<month_id>[\w\-]+)/$', views.months, name='months'),
#    # /budget/<budget.id>/favorite, does some logic and sends back
#    url(r'^(?P<month_id>[\w\-]+)/$', views.months, name='months'),
#    # /budget/generic.html
#    url(r'^generic.html$', views.generic, name='generic'),
#    # /budget/elements.html
#    url(r'^elements.html$', views.elements, name='elements'),
#    # /budget/all_months.html
#    url(r'^all_months.html$', views.all_months, name='all_months'),



    ##################   NEW     ####################
    #/budget/
    url(r'^$', views.index, name='index'),
    
    # /budget/track
    url(r'^track$', views.track, name='track'),
    
    # /budget/analyze
    url(r'^analyze$', views.analyze, name='analyze'),
    
    # /budget/take-action
    url(r'^action$', views.action, name='action'),    
]

from django.conf.urls import patterns, url

from wallet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account/', views.account, name='account'),
    url(r'^send/', views.send, name='send'),
    url(r'^transactions/', views.transactions, name='transactions'),
    url(r'^assets/', views.assets, name='assets'),
)

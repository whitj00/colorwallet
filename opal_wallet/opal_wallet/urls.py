from django.contrib.auth.views import login
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^register/', 'registration.views.register', name='register'),
    url(r'^login/', 'django.contrib.auth.views.login', {'extra_context':{'next':'/update/'}}, name='login'),
    url(r'^logout/', 'registration.views.logout', name='logout'),
    url(r'^update/', 'wallet.views.update', name='update'),
    url(r'^u/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('wallet.urls')),
)

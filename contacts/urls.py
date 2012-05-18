from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('contacts.views',
    url(r'^$', 'contact_list', name='contact_list'),
    url(r'^add/$', 'contact_add', name='contact_add'),
    url(r'^(?P<person_id>\d+)/$', 'contact_view', name='contact_view'),
    url(r'^(?P<person_id>\d+)/edit/$', 'contact_edit', name='contact_edit'),

)

# from django.conf.urls import include, url
# from quoteweb import settings

# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


from django.conf.urls import url
from django.contrib import admin
from randomg.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', generate),

]

urlpatterns += staticfiles_urlpatterns()

# urlpatterns = patterns('',
#     # Examples:
#     url(r'^$', 'randomg.views.generate'),
#     # url(r'^quoteweb/', include('quoteweb.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# )


# urlpatterns = [
#     # Examples:
#     url(r'^$', 'randomg.views.generate'),
#     # url(r'^quoteweb/', include('quoteweb.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# ]

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EuroDrivers.views.home', name='home'),
    # url(r'^EuroDrivers/', include('EuroDrivers.foo.urls')),
	url(r'^$', 'eurodrivers_app.views.main'),
	url(r'^setlang/(?P<lang_id>\d+)$', 'eurodrivers_app.views.setlang'),
	url(r'^addcomment/$', 'eurodrivers_app.views.addOpinion'),
	url(r'^getcomments/$', 'eurodrivers_app.views.comments_to_pdf'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'i18n/',include('django.conf.urls.i18n'))
)

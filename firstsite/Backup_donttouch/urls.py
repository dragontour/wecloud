"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls import include, url
from firstsite.wec.views import main, login_error, dashboard, pmain, mmain, test, fill, graph, web
from firstsite.wec.views_webpage import web_1
from firstsite.wec.db import create_webtable, page_set
from firstsite.wec.views2 import thanks, login, register, members_db, membersdel, emailtest, services, about, contact
from firstsite.wec.views2 import registration, fade,pc,mobile, ssize, members_features,picture
from firstsite.wec.ipic import image_setup, image_write
from firstsite.wec.views_website import image_update
from firstsite.wec.views_picture import image_upload
from firstsite.wec.views_admin import admin_add_users, display_users
from firstsite.wec.views_test import create_table

from firstsite.wec.we_scheduler import matrix, mainadd, maindel, matrice, imain, db, main_new
#from firstsite.wec.db1 import member
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
        url(r'^$', main),
        url(r'^web/(?P<addy>\w{0,50})',web),
        url(r'^table/',create_webtable),
        url(r'^pageset/',page_set),
        url(r'^login/',login),
        url(r'^emailtest/',emailtest),
        url(r'^register/',register),
        url(r'^fill/',fill),
        url(r'^feature/',members_features),
        url(r'^pc/',pc),
        url(r'^pmain/',pmain),
        url(r'^ssize/get/(?P<wid>\d+)/(?P<hei>\d+)/$',ssize),
        url(r'^mmain/',mmain),
        url(r'^up/',image_upload),
        url(r'^update/',image_update),
        url(r'^mobile/',mobile),
        url(r'^about/',about),
        url(r'^contact/',contact),
        url(r'^services/',services),
        #url(r'^member/$', member),
        url(r'^fade/$', fade),
        url(r'^login_error/$', login_error),
        url(r'^dashboard/$', dashboard),
        url(r'^thanks/', thanks),
        url(r'^test/$', test),
        #url(r'^dm/$', dm),
        url(r'^imain/$', imain),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^mainadd/$', mainadd),
        url(r'^matrix/$', matrix),
        url(r'^main_new/$', main_new),
        url(r'^db/$', db),
        url(r'^members_db/$', members_db),
        url(r'^picture/$', picture),
        #url(r'^registration/$', registration),
        url(r'^members_db/get/(?P<db_id>\d+)/$', membersdel),
        url(r'^db/get/(?P<db_id>\d+)/$', maindel),
        url(r'^registration/get/(?P<db_id>\d+)/$', registration),
        url(r'^matrice/get/(?P<index>\d+)/$', matrice),
        url(r'^image/',image_setup),
        url(r'^imagecheck/',image_write),
		url(r'^graph/',graph),
        url(r'^create/',create_table),
# ************ Admin Add Ons ******************************************
        url(r'^admin_add_users/',admin_add_users),
        url(r'^display_users/',display_users),
# *********************************************************************   
# ************ WebPage Templates ******************************************   
        url(r'^web_1/',web_1),
    
    
# *********************************************************************     
]



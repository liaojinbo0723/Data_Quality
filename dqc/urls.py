#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.conf.urls import url
from . import views

app_name = "dqc"
urlpatterns = [
	url(r'^$', views.dqc_login, name='login'),
	url(r'^del_rule$', views.dqc_del, name='del'),
	url(r'^add_rule$', views.dqc_add, name='add'),
	url(r'^edit_rule$', views.dqc_edit, name='edit'),
	url(r'^search$', views.dqc_search, name='search'),
	url(r'^index$', views.index, name='index'),
]
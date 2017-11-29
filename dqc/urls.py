#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^del_rule$', views.dqc_del, name='del'),
	url(r'^add_rule$', views.dqc_add, name='add'),
	url(r'^edit_rule$', views.dqc_edit, name='edit'),
	url(r'^base$', views.dqc_base, name='base'),
]
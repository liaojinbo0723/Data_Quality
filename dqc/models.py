# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Alarmconf(models.Model):
	app_name = models.CharField(max_length=50)
	job_name = models.CharField(max_length=100)
	db_name = models.CharField(max_length=20)
	table_name = models.CharField(max_length=50)
	file_dir = models.CharField(max_length=50)
	static_column = models.CharField(max_length=100)
	error_alarm = models.CharField(max_length=10)
	date_week = models.CharField(max_length=100)
	date_alarm = models.CharField(max_length=10)
	owner = models.CharField(max_length=50)
	mobile = models.CharField(max_length=50)
	valid_flag = models.CharField(max_length=50)

class UserInfo(models.Model):
	user_name = models.CharField(max_length=20,unique=True)
	user_pass = models.CharField(max_length=20)
	is_admin = models.BigIntegerField()
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

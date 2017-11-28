# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Alarmconf
from django.template import loader
from django.shortcuts import redirect

# Create your views here.

def index(request):
	dqc_list = Alarmconf.objects.all()
	context = {
		"dqc_list":dqc_list
	}
	return render(request,"index.html",context)

def dqc_del(request):
	nid = request.GET.get('nid')
	Alarmconf.objects.filter(id=nid).delete()
	return redirect('/dqc')

def dqc_add(request):
	if request.method == "GET":
		return render(request,"add_rule.html")
	elif request.method == "POST":
		app_name = request.POST.get("app_name")
		job_name = request.POST.get("job_name")
		db_name = request.POST.get("db_name")
		table_name = request.POST.get("table_name")
		file_dir = request.POST.get("file_dir")
		static_column = request.POST.get("static_column")
		error_alarm = request.POST.get("error_alarm")
		date_week = request.POST.get("date_week")
		date_alarm = request.POST.get("date_alarm")
		owner = request.POST.get("owner")
		mobile = request.POST.get("mobile")
		valid_flag = request.POST.get("valid_flag")
		Alarmconf.objects.create(app_name = app_name,
								 job_name = job_name,
								 db_name = db_name,
								 table_name = table_name,
								 file_dir = file_dir,
								 static_column = static_column,
								 error_alarm = error_alarm,
								 date_week = date_week,
								 date_alarm = date_alarm,
								 owner = owner,
								 mobile = mobile,
								 valid_flag = valid_flag)
		return redirect('/dqc')


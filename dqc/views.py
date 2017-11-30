# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Alarmconf
from django.template import loader
from django.shortcuts import redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.


def index(request):
	dqc_list = Alarmconf.objects.all()
	context = {
		"dqc_list":dqc_list
	}

	pn = Paginator(dqc_list, 12)
	page = request.GET.get('page', 1)
	cur_page = int(page)

	try:
		print(page)
		dqc_list = pn.page(page)
	except PageNotAnInteger:
		dqc_list = pn.page(1)
	except EmptyPage:
		dqc_list = pn.page(pn.num_pages)
	"""locals()返回的字典对所有局部变量的名称与值进行映射"""
	return render(request, "index.html", locals())

def dqc_base(request):
	dqc_list = Alarmconf.objects.all()
	context = {
		"dqc_list": dqc_list
	}
	return render(request, "base.html", context)

def dqc_del(request):
	nid = request.GET.get('nid')
	Alarmconf.objects.filter(id=nid).delete()
	return redirect('/dqc')

def dqc_add(request):
	if request.method == "GET":
		return render(request, "add_rule.html")
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

def dqc_edit(request):
	if request.method == "GET":
		nid = request.GET.get('nid')
		query_set = Alarmconf.objects.filter(id=nid).first()
		context = {
			"dqc_list": query_set
		}
		return render(request, "edit_rule.html", context)
	elif request.method == "POST":
		nid = request.GET.get('nid')
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
		Alarmconf.objects.filter(id=nid).update(app_name = app_name,
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


def dqc_search(request):
	text = request.GET.get('a')
	# print "text:{}".format(text)
	# print request.get_full_path()
	if text == None or text == "":
		dqc_list = Alarmconf.objects.all()
	else:
		"""多条件模糊匹配"""
		dqc_list = Alarmconf.objects.filter(Q(app_name__icontains=text)|Q(job_name__icontains=text)|Q(db_name__icontains=text)|Q(table_name__icontains=text)|Q(owner__icontains=text)|Q(mobile__icontains=text))

	pn = Paginator(dqc_list, 12)
	page = request.GET.get('page', 1)
	cur_page = int(page)

	try:
		print(page)
		dqc_list = pn.page(page)
	except PageNotAnInteger:
		dqc_list = pn.page(1)
	except EmptyPage:
		dqc_list = pn.page(pn.num_pages)
	"""这里要把搜索框的关键字传给前端,不然搜索翻页会有问题"""
	context = {
		"dqc_list": dqc_list,
		"param_input": text
	}
	"""locals()返回的字典对所有局部变量的名称与值进行映射"""
	return render(request, "index.html", context)
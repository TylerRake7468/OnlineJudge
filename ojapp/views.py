from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Problem

def home(request):
	return render(request, "ojapp/index.html")

def problems(request):
	problems = Problem.objects.all()
	context = {
		'problems': problems, 
	}
	return render(request, "ojapp/problems.html", context)

def show_problem(request, id):
	return render(request, "ojapp/problem_show.html")

def login_page(request):
	return render(request, "ojapp/signup_page.html")
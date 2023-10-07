from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Problem, User, TestCase
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login
from .forms import SubmissionLogForm
import pdb
import docker

def home(request):
	return render(request, "ojapp/index.html")

def problems(request):
	problems = Problem.objects.all()
	context = {
		'problems': problems, 
	}
	return render(request, "ojapp/problems.html", context)

def show_problem(request, id):
	problem = Problem.objects.get(id=id)

	return render(request, "ojapp/problem_show.html", {'problem': problem})

def verdict_page(request, id):
	if request.method == 'POST':
		# form = SubmissionLogForm(request.POST)
		# pdb.set_trace()
		# docker_client = docker.from_env()
		# Running = "running"

		# problem = Problem.objects.get(id=id)
		# testcase = TestCase.objects.get(problem_id=id)
		# testcase.output = testcase.output.replace('\r\n','\n').strip()

		# if problem.difficulty=="Easy":
		# 	score = 10
		# elif problem.difficulty=="Medium":
		# 	score = 30
		# else:
		# 	score = 50

		# verdict = "Wrong Answer"
		# res = ""
		# run_time = 0

		# user_code = ''
		return render(request, "ojapp/verdict_page.html")

def login_handle(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = User.objects.filter(UserName=str(username)).values()[0]
		if len(user)!=0:
			if check_password(str(password), user['Password']):
				request.session['user_id'] = user['UserId']
				# pdb.set_trace()
				return redirect("home")
			else:
				return render(request, "ojapp/login.html",{'error_message': "Incorrect Password !!!"})
		else:
			return render(request, "ojapp/login.html",{'error_message': "User not Fount !!!"})
	return render(request, "ojapp/login.html")

def signup_handle(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']

		if pass1 != pass2:
			return render(request, "ojapp/signup.html", {'error_message':"Password not match !!!"})

		user = User.objects.create(UserName=username, Email=email, Password=make_password(pass1))
		user.save()

		return redirect("login_page")
	return render(request, "ojapp/signup.html")

def logout_handle(request):
	if 'user_id' in request.session:
		del request.session['user_id']
	return redirect("login_page")

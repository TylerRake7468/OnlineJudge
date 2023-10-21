from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Problem, User, TestCase, SubmissionLog
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login, authenticate, logout
from .forms import CodeForm
from time import time
from datetime import datetime
import pdb
import docker
import os
import signal
import subprocess
import os.path

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
	form = CodeForm()
	return render(request, "ojapp/problem_show.html", {'problem': problem, 'code_form': form})

def verdict_page(request, id):
    if request.method == 'POST':
        docker_client = docker.from_env()
        Running = "running"
        user_code = ''
        form = CodeForm(request.POST)
        if form.is_valid():
        	user_code = form.cleaned_data.get('code')
        	user_code = user_code.replace('\r\n','\n').strip()
        problem = Problem.objects.get(id=id)

        # score of a problem
        if problem.difficulty=="Easy":
            score = 10
        elif problem.difficulty=="Medium":
            score = 30
        else:
            score = 50

        #setting verdict to wrong by default
        verdict = "Wrong Answer" 
        res = ""
        run_time = 0
        # pdb.set_trace()
        language = request.POST.get('language_val')
        pdb.set_trace()
        user = User.objects.get(id=request.session['user_id'])
        submission_log = SubmissionLog(user=user, problem=problem, submitted_at=datetime.now(), language=language, code=user_code)
        submission_log.save()

        file_name = str(submission_log.id)

		
        if language == "C++":
            extension = ".cpp"
            cont_name = "oj-cpp"
            compile = f"g++ -o {filename} {filename}.cpp"
            clean = f"{filename} {filename}.cpp"
            docker_img = "gcc:11.2.0"
            exe = f"./{filename}"
            
        elif language == "C":
            extension = ".c"
            cont_name = "oj-c"
            compile = f"gcc -o {filename} {filename}.c"
            clean = f"{filename} {filename}.c"
            docker_img = "gcc:11.2.0"
            exe = f"./{filename}"

        elif language == "Python3":
            extension = ".py"
            cont_name = "oj-py3"
            compile = "python3"
            clean = f"{filename}.py"
            docker_img = "python3"
            exe = f"python {filename}.py"
        
        elif language == "Python2":
            extension = ".py"
            cont_name = "oj-py2"
            compile = "python2"
            clean = f"{filename}.py"
            docker_img = "python2"
            exe = f"python {filename}.py"

        elif language == "Java":
            filename = "Main"
            extension = ".java"
            cont_name = "oj-java"
            compile = f"javac {filename}.java"
            clean = f"{filename}.java {filename}.class"
            docker_img = "openjdk"
            exe = f"java {filename}"

		# file = file_name + extension

		# file_path = settings.FILE_DIR

        return render(request, "ojapp/verdict_page.html", {'code': user_code})


def login_handle(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # request.session['user_id'] = user.id
                login(request, user)
                return redirect("home")
            else:
                return render(request, "ojapp/login.html", {'error_message': "Incorrect Password !!!"})
        except User.DoesNotExist:
            return render(request, "ojapp/login.html", {'error_message': "User not found !!!"})
    return render(request, "ojapp/login.html")

def signup_handle(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']

		if pass1 != pass2:
			return render(request, "ojapp/signup.html", {'error_message':"Password not match !!!"})

		user = User.objects.create(username=username, email=email, password=make_password(pass1))
		user.save()

		return redirect("login_page")
	return render(request, "ojapp/signup.html")

def logout_handle(request):
    logout(request)
    return redirect("login_page")
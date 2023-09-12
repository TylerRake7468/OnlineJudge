from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Problem, User

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

def login_handle(request):
	return render(request, "ojapp/login.html")

def signup_handle(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']

		if pass1 != pass2:
			return render(request, "ojapp/signup.html", {'error_message':"Password not match !!!"})

		user = User.objects.create(UserName=username, Email=email, Password=pass1)
		user.save()

		return redirect("login_page")
	return render(request, "ojapp/signup.html")
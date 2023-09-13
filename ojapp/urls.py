from django.urls import path
from . import views


urlpatterns = [
	path("", views.home, name = "home"),
	path("login", views.login_handle, name="login_page"),
	path("signup", views.signup_handle, name="signup_page"),
	path("problems", views.problems, name = "problems"),
	path("problems/<int:id>", views.show_problem, name = "show_problem"),
	path("logout", views.logout_handle, name="logout"),
]
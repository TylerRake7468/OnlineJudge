from django.urls import path
from . import views


urlpatterns = [
	path("", views.home, name = "home"),
	path("login", views.login_page, name="login_page"),
	path("problems", views.problems, name = "problems"),
	path("problems/<int:id>", views.show_problem, name = "show_problem"),
]
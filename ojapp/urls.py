from django.urls import path
from . import views


urlpatterns = [
	path("", views.home, name = "home"),
	path("problems", views.problems, name = "problems"),
	path("problems/<int:id>", views.show_problem, name = "show_problem"),
]
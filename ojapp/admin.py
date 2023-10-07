from django.contrib import admin

from .models import User, Problem, SubmissionLog, TestCase

admin.site.register(User)
admin.site.register(Problem)
admin.site.register(SubmissionLog)
admin.site.register(TestCase)

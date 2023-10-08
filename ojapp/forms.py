from django import forms
from django.forms import ModelForm
from .models import SubmissionLog

class SubmissionLogForm(ModelForm):
	class Meta:
		model = SubmissionLog
		fields = ['code']
		widgets = {'code' : forms.Textarea()}
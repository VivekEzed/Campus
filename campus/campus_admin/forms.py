from django import forms
from .models import Offers,Posts

class FileForm(forms.Form):
	image=forms.FileField()
class FileFormPost(forms.Form):
	image=forms.FileField()
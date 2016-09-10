from django import forms

class EClientForm(forms.Form):
	name = forms.CharField(max_length=10)
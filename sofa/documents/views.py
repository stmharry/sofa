from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from documents.forms import EClientForm

class EClientService(View):
	def get(self, request):
		return render(request, 'documents/base.html', {'form': EClientForm()})
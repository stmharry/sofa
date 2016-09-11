from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class ElectronicView(View):
	def get(self, request):
		return render(request, 'documents/base.html')


class PaperView(View):
    def get(self, request):
        return render(request, 'documents/base.html')


class CreateView(View):
    def get(self, request):
        return render(request, 'documents/base.html')


class FileView(View):
    def get(self, request):
        return render(request, 'documents/base.html')
from django.shortcuts import render
from . import settings

def index(request, *args, **kwargs):
	print(settings.STATIC_ROOT)
	return render(request, 'dist/index.html')

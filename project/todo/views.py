from django.shortcuts import render
from .forms import AddForm
# Create your views here.

def index(req):
    return render(req, 'index.html')

def add(request):
    add = AddForm()
    return render(request, 'add.html', {'form': add})
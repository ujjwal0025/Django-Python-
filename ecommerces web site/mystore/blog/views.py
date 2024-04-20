from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import blogger

# Create your views here.
def index(request):
    allblog = blogger.objects.all()
    return render(request,'blog/index.html',{'allblog':allblog})

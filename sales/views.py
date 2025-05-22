from django.shortcuts import render
from django.http import request




# Create your views here.
def sales(request):
    return render(request,'sales/index.html')


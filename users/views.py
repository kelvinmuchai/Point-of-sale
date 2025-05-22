from django.shortcuts import render,redirect
from .forms import usercreateform

def register(request):          
    if request.method == "POST":
        form = usercreateform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = usercreateform()
    return render(request,'users/register.html',{'form':form})


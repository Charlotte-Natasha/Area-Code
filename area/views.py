from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *

def index(request):

    return render(request, 'area/index.html')

def sign_up(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
        
        
    #     user = User.objects.create_user(username=username, email=email, password=password)

    #         return redirect('login')

    # else:  
        return render(request, 'registration/signup.html', {})      

def profile(request):

    return render(request, 'area/profile.html')  

def editprofile(request):
    if request.method == 'POST':
        # logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'area/editprofile.html', {'form':form})  
            
def areahood(request):

    return render(request, 'area/areahood.html')             
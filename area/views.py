from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *

def index(request):

    return render(request, 'area/index.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
            
        user = User.objects.create_user(username=username, email=email, password=password)

        return redirect('login')

    else:  
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
    all_neighborhoods = Neighborhood.get_all_neighborhoods()
    print(all_neighborhoods)
    return render(request, 'area/areahood.html', {'all_neighborhoods': all_neighborhoods})  

def business(request):

    return render(request, 'area/business.html')  

def new_business(request):
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Admin = current_user
            project.admin_profile = profile
            project.save()
        return redirect('index')

    else:
        form = NewBusinessForm()
    return render(request, 'new-business.html', {"form": form})     
                    

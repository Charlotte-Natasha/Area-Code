from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

def index(request):
    
    return render(request, 'area/index.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image)
        user.save()
        profile.save()

        if profile:
            return redirect('login')

    else:  
        return render(request, 'registration/signup.html', {})      

@login_required(login_url="/login")
def profile(request):
    user = request.user
    profile = Profile.objects.get( user = user)

    return render(request, 'area/profile.html', {'profile':profile, 'user':user})  

@login_required(login_url="/login")
def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'area/editprofile.html', {'form':form})  

@login_required(login_url="/login")            
def areahood(request):
    all_neighborhoods = Neighborhood.objects.all()
    print(all_neighborhoods)
    return render(request, 'area/areahood.html', {'all_neighborhoods': all_neighborhoods})  

@login_required(login_url="/login")
def business(request):
    business = Business.objects.all()

    return render(request, 'area/business.html', {'business':business})  

@login_required(login_url="/login")
def new_business(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile
            project.user_profile = profile
            project.save()
        return redirect('business')

    else:
        form = NewBusinessForm()
    return render(request, 'area/new-business.html', {"form": form}) 

@login_required(login_url="/login")
def addhood(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == "POST":
        form = AddhoodForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile
            project.save()
            
            return redirect('areahood')
    else:
        form = AddhoodForm()     
    return render(request, 'area/addhood.html', {'form':form})         

@login_required(login_url="/login")
def join_hood(request, id):
    neighborhood = Neighborhood.objects.get(id=id)
    request.user.userprofile.neighborhood = neighborhood
    request.user.userprofile.save()
    return redirect('neighborhood')                    

@login_required(login_url="/login")
def leave_hood(request, id):
    hood = Neighborhood.objects.get(id=id)
    request.user.userprofile.neighborhood = None
    request.user.userprofile.save()
    return redirect('neighborhood')
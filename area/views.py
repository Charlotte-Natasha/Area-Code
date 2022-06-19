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
        image = request.FILES.get('image')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image)
        user.save()
        profile.save()

        if profile:
            return redirect('login')

    else:  
        return render(request, 'registration/signup.html', {})      

def profile(request):
    user = request.user
    profile = Profile.objects.get( user = user)

    return render(request, 'area/profile.html', {'profile':profile, 'user':user})  

def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'area/editprofile.html', {'form':form})  
            
def areahood(request):
    all_neighborhoods = Neighborhood.objects.all()
    print(all_neighborhoods)
    return render(request, 'area/areahood.html', {'all_neighborhoods': all_neighborhoods})  

def business(request):
    business = Business.objects.all()

    return render(request, 'area/business.html', {'business':business})  

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

def addhood(request):
    # form = AddhoodForm()
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == "POST":
        form = AddhoodForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = profile
            # project.user_profile = profile
            project.save()
            # name = form.cleaned_data['name']
            # location = form.cleaned_data['location']
            # image = form.cleaned_data['image']
            # data = Neighborhood.objects.create(
            #     name=name, user=request.user, location=location, image=image)
            # data.save()
            return redirect('areahood')
    # context = {'form': form}   
    else:
        form = AddhoodForm()     
    return render(request, 'area/addhood.html', {'form':form})         
                    

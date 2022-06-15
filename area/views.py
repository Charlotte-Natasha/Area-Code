from django.shortcuts import render

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
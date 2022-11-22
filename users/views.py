from glob import glob
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm 
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def profiles(request):
    if request.user.is_authenticated:
        currentUser = request.user.profile
        context = {'user':currentUser}
        return render(request, 'users/profile.html', context)
    else:
        return render(request, 'users/loginpage.html')

def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile')            
        else:
            messages.error(request, 'Invalid entry to the form!')

    form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'users/registerpage.html', context)

def loginUser(request):
    if(request.method == 'POST'):
        useremail = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username=useremail)
        except:
            messages.error(request, "User does not exist!")
            return render(request, 'users/loginpage.html')
        
        user = authenticate(request, username = useremail, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Email or password incorrect")
        
    return render(request, 'users/loginpage.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
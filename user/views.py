from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import registerForm

'''
user given username and password, it passed into authenticate function 
if user is exist then authenicate function return an user otherwise its
return none
'''
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', {})

'''
user given their information and its passed to registerForm
if all information is valid then save the user and also login
'''
def registerView(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'register.html', {'form': form})


'''
if user exist in our session then logout function 
just remove it from our session and redirct to login
'''
@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('login')

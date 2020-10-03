from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            print('done')
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)
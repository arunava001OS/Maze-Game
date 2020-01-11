from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def index(request):
	return render(request,'game/index.html',{})


def signup(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			return redirect('login')
	else:
		form=UserForm()
	args={'form': form}
	return render(request,'game/signup.html',args)


def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('index2')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'game/login.html',context)

@login_required
def logout_view(request):
	logout(request)
	return render(request,'game/index.html',{})



from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib import messages


from . models import Profile
from . forms import(
	LoginForm,
	UserRegistrationForm,
	UserEditForm,
	ProfileEditForm)

def loginView(request):
	if request.method =='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('product_list')
				else:
					return HttpResponse("dissabled account")
			else:
				messages.error(request,"password or username does not exist")

	else:
		form =LoginForm()
	return render(request,'shop/account/logint.html',{'form':form})
def logout(request):
	logout(request)
	return redirect('logint')
def userRegistration (request):
	if request.method == 'POST':
		user_form =  UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)			
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return redirect('logint')
	else:
		user_form =UserRegistrationForm()
	return render(request,'shop/account/register.html', {'user_form':user_form})

@login_required
def editProfile(request):
	if request.method == 'POST':
		reg_form = UserEditForm(instance=request.user, data=request.POST)
		prof_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
		if reg_form and prof_form.is_valid():
			reg_form.save()
			prof_form.save()
	else:
		reg_form =UserEditForm(instance=request.user)
		prof_form = ProfileEditForm()
	return render(request,'shop/account/editProfile.html',{'reg_form':reg_form,'prof_form':prof_form})
# view to change password

def PasswordChange(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, data=request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'password changed successfully')
		else:
			messages.error(request,'password cannot be cahnged')
	else:
		form= PasswordChangeForm(request.user)
	return render(request,'regist/change-password.html',{'form':form})

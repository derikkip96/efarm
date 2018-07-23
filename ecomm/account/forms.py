from django import forms
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
	username = forms.CharField(required=True,widget=forms.TextInput( attrs={'class':'form-control','placeholder':'username'}))
	password = forms.CharField(widget=forms.PasswordInput( attrs={'class':'form-control','placeholder':'*******'}))

class UserRegistrationForm(forms.ModelForm):
	password= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
	first_name=forms.CharField(label='First Name',widget=forms.TextInput( attrs={'class':'form-control','placeholder':'First Name'}))
	last_name=forms.CharField(label='Last Name',widget=forms.TextInput( attrs={'class':'form-control','placeholder':'Last Name'}))
	username= forms.CharField(label='Username',widget=forms.TextInput( attrs={'class':'form-control','placeholder':'username'}))
	email = forms.CharField(label='Email',widget=forms.TextInput( attrs={'class':'form-control','placeholder':'Email'}))

	class Meta:
		model=User
		fields =('first_name','last_name','username','email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password']!=cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']
class UserEditForm(forms.ModelForm):

	class Meta:
		model = User
		fields =('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
	image=forms.ImageField()
	class Meta:
		model = Profile
		fields = ('date_of_birth','image')



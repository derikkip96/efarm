from django import forms
from . models import Order
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
		widgets={
			'first_name': forms.TextInput(attrs={'class': 'input'}),
			'last_name': forms.TextInput(attrs={'class': 'input'}),
			'email': forms.EmailInput(attrs={'class': 'input'}),
			'address': forms.TextInput(attrs={'class': 'input'}),
			'postal_code': forms.TextInput(attrs={'class': 'input'}),
			'city': forms.TextInput(attrs={'class': 'input'}),

		}
	
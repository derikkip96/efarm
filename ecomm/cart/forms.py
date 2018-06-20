from django import forms

PRODUCT_QUANTITY_CHOICE=[(i, str(i)) for i in range(1,21)]
class shoping(forms.Form):
	update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
	quantity=forms.TypedChoiceField(required=True,
									 choices=PRODUCT_QUANTITY_CHOICE, 
									 coerce =int)

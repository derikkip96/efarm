# from django import forms
#
# INPUT_QUANTITY_CHOICE=[(i, str(i)) for i in range(1,5)]
#
# class HireForm(forms.Form):
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
#     quantity=forms.TypedChoiceField(required=False,
#                                     choices=INPUT_QUANTITY_CHOICE,
#                                     coerce=int
#                                     )
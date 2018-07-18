from django import forms
from . models import  Question,Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['ask_question',]
        widgets={'ask_question': forms.Textarea(attrs={'class':'input'})}
class AnswerForm(forms.ModelForm):

    class Meta:
        model=Answer
        fields=('body',)
        widgets={
            'body':forms.Textarea(attrs={'class':'form','placeholder':'answer here'})
        }

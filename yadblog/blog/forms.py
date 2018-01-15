from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder': 'Name',
                'class' : 'form-control text-muted',
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class' : 'form-control text-muted',
            }),
            'body' : forms.Textarea(attrs={
                'placeholder': 'Leave Your Comment Here...',
                'class' : 'form-control text-muted',
            }),
        }

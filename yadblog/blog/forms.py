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

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class' : 'form-control text-muted',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class' : 'form-control text-muted',
        }),
    )
    subject = forms.CharField(max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class' : 'form-control text-muted',
                        })
                    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Message Here...',
            'class' : 'form-control text-muted',
        }),
    )

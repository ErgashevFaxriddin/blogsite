from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Post maydoni formda bo‘lmasin — view’da biriktiriladi
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'body': forms.Textarea(attrs={'placeholder': 'Izohingiz...'}),
        }

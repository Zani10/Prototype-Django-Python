from django import forms 
from .models import Article 
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))

    class Meta:
        model = Article
        fields = ['title', 'content', 'custom_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None 
        self.fields['password2'].help_text = None  
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password'
        })